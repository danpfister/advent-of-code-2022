# Advent of Code 2022
-----
Solving the [Advent of Code 2022](https://adventofcode.com/2022) with Python 3.10

## Advent of Code Helper
The `aoc_helper.py` allows automatic downloading of the current input file and creates an empty python script for the current day.

### Usage
Before usage, the session cookie needs to be stored in a file `config.json` in following format:
```
{
    "session_cookie": "your-session-cookie-here"
}
```
An optional parameter `--day` can be passed to force the download for a specific day. Running
```
python aoc_helper.py --day 5
```
downloads the input file and creates a python script for day 5.

Alternatively, the setup can be run from the powershell script `aoc_setup.ps1` with following syntax:
```
& aoc_setup.ps1 -day 5
```