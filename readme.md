cmd 
for /f "delims=" %%a in (.env) do set %%a
powershell
Get-Content .env | ForEach-Object { $key, $value = $_ -split '=',2; [System.Environment]::SetEnvironmentVariable($key, $value, [System.EnvironmentVariableTarget]::Process) }

env/Scripts/activate
python -m pip install dbt-sqlserver

If you're working within a team or need the profile to be part of your project for CI/CD purposes, you can specify a custom location for the profiles.yml file within your project directory and reference it when running dbt commands using the --profiles-dir option.