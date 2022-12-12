param (
    [parameter(mandatory=$false)][int]$day
)

Write-Host "starting advent of code setup"

$script_dir = Split-Path $MyInvocation.MyCommand.Path -Parent
$py_path = Join-Path -Path $script_dir -ChildPath "aoc_helper.py"

if ($PSBoundParameters.ContainsKey('day') -eq $true) {
    python.exe $py_path --day $day
}
else {
    python.exe $py_path
}

Write-Host "setup completed"