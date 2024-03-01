 <div align="center">
  <p>
      <img src="https://github.com/Wemmy/BI-with-Outlook-and-dbt/blob/master/BI_with_outlook.png"></a>
  </p>
</div>

# Automated Report Update with Outlook

## Introduction
This project automates the update process of reports by integrating various tools including Power Automate, Python, dbt (data build tool), and GitHub Actions. The automation pipeline is designed to streamline the update of reports by fetching data from outlook, processing it through a local SQL server, and finally generating the desired tables for Power BI reporting.

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Dependencies](#dependencies)
- [Configuration](#configuration)
- [Documentation](#documentation)
- [Examples](#examples)


## Installation
This section outlines the steps required to set up the necessary tools and environment for the project.

### Prerequisites
- Power Automate
- Python
- dbt
- GitHub account with Actions enabled
- SQL Server

### Setup
1. **Power Automate**: Ensure you have access to Power Automate and configure it to download Excel files from emails to a OneDrive folder.
2. **Python**: Install Python and ensure it's properly configured on your system.
3. **dbt**: Follow the [official dbt installation guide](https://docs.getdbt.com/dbt-cli/installation) to install dbt.
4. **GitHub Actions**: No installation required, but familiarize yourself with [GitHub Actions documentation](https://docs.github.com/en/actions).

## Usage
To use this project, follow these steps:

1. **Email to OneDrive**: Configure Power Automate to automatically download the required Excel files from your email to a specified OneDrive folder.
2. **Excel to SQL Server**: Use the provided Python script to upload Excel files from the OneDrive folder to a local SQL Server.
3. **Generate Tables with dbt**: Use dbt to transform your data and generate the desired tables for Power BI reports.
4. **Automate with GitHub Actions**: Set up GitHub Actions to automate the entire process, ensuring your Power BI reports are always up to date.

## Features
- Automated extraction of Excel files from emails
- Seamless data upload from Excel to SQL Server
- Automated data transformation and table generation with dbt
- Continuous integration and deployment with GitHub Actions

## Dependencies
- Power Automate for Excel file extraction
- Python for data processing
- SQL Server as the data storage solution
- dbt for data transformation
- GitHub Actions for automation

## Configuration
Details on how to configure each component of the project can be found in their respective documentation. Ensure all configurations are secure and optimized for your specific environment.

## Documentation
Further documentation for each tool used in this project can be found at their official websites:
- [Power Automate Documentation](https://docs.microsoft.com/en-us/power-automate/)
- [Python Documentation](https://docs.python.org/3/)
- [dbt Documentation](https://docs.getdbt.com/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)

## Examples
Include any examples of how to run scripts, configure workflows, or any other useful examples for using this project.



cmd 
for /f "delims=" %%a in (.env) do set %%a
powershell
Get-Content .env | ForEach-Object { $key, $value = $_ -split '=',2; [System.Environment]::SetEnvironmentVariable($key, $value, [System.EnvironmentVariableTarget]::Process) }

env/Scripts/activate
python -m pip install dbt-sqlserver

If you're working within a team or need the profile to be part of your project for CI/CD purposes, you can specify a custom location for the profiles.yml file within your project directory and reference it when running dbt commands using the --profiles-dir option.