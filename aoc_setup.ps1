Write-Host "starting advent of code setup for current day"

$script_dir = Split-Path $MyInvocation.MyCommand.Path -Parent
$py_path = Join-Path -Path $script_dir -ChildPath "aoc_helper.py"

python.exe $py_path

Write-Host "setup completed"