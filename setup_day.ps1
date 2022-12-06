Write-Host "downloading input and creating python file for today"

$script_dir = Split-Path $MyInvocation.MyCommand.Path -Parent
$py_path = Join-Path -Path $script_dir -ChildPath "aoc_input_fetcher.py"

python.exe $py_path

Write-Host "setup completed"