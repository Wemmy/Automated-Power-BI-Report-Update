from dataclasses import dataclass
from sqlalchemy.engine import Engine
from pandas import DataFrame
from numpy import nan
from textwrap import dedent

CHUNKSIZE = 500

@dataclass(frozen=True)
class ImportableExcelSheet:
    """
    A dataclass to represent a sheet from the excel file to be uploaded.
    
    Attributes:
        - sheet_name: the name of the sheet in the excel file.
        - target_relation: the name of the view the data should be 
                           surfaced in. the history table will take the same 
                           name, but suffixed with "_history".
    """

    sheet_name: str
    target_schema: str
    target_relation: str

    @property
    def latest_file_view(self):
        return self.target_relation
    
    @property
    def history_table(self):
        return f"{self.target_relation}_history"


def _create_target_schema_if_not_exists(engine: Engine, schema: str) -> None:
    """Ensures the TARGET_SCHEMA is created if it does not already exist."""

    print(
        f"\nCreating the '{schema}' schema "
        "if it does not already exist..."
    )
    
    with engine.begin() as conn:
        conn.exec_driver_sql(f"CREATE SCHEMA IF NOT EXISTS {schema};")


def _df_columns_to_snake_case(df: DataFrame) -> DataFrame:
    """Converts a dataframe's columns to snake case."""

    df.columns = (
        df.columns
        .str.replace(' ', '_', regex=True)
        .str.replace(r'[^A-Za-z0-9_]+', '', regex=True)
        .str.lower()
    )

    return df

def _df_blanks_to_nans(df: DataFrame) -> DataFrame:
    """
    Replaces all empty strings, or strings filled with solely 
    whitespace, to np.nan.
    """

    df = df.replace(r'^\s*$', nan, regex=True)

    return df

def _write_dataframe_to_sqlserver(
    df: DataFrame,
    engine: Engine,
    sheet: ImportableExcelSheet,
) -> None:
    """Writes the dataframe to the target history table in Snowflake."""

    print(
        "\nWriting dataframe to Snowflake table "
        f"'{sheet.target_schema}.{sheet.history_table}'..."
    )

    _create_target_schema_if_not_exists(engine, sheet.target_schema)

    df.to_sql(
        con=engine,
        schema=sheet.target_schema,
        name=sheet.history_table,
        if_exists='replace',
        method="multi",
        index=False,
        chunksize=CHUNKSIZE,
    )


def _create_latest_file_view(
    engine: Engine,
    sheet: ImportableExcelSheet,
) -> None:
    """Creates a view to surface only the latest file from the history table."""

    print(f"\nCreating a view to surface the lastest file uploaded...")

    latest_view = f"{sheet.target_schema}.{sheet.latest_file_view}"
    history_table = f"{sheet.target_schema}.{sheet.history_table}"

    query =  dedent(
        f"""\
            CREATE OR REPLACE VIEW {latest_view} AS (
                SELECT *
                FROM {history_table} AS history
                WHERE history.etl_extract_timestamp = (
                    SELECT MAX(etl_extract_timestamp)
                    FROM {history_table}
                )
            );
        """
    )
    
    with engine.begin() as conn:
        conn.exec_driver_sql(query)