# Advent of Code 2022
-----
Solving the [Advent of Code 2022](https://adventofcode.com/2022) with Python 3.10

## Advent of Code Download Helper
The `aoc_helper.py` allows automatic downloading of the current input file and creates an empty python script for the current day.

### Usage
Before usage, the [session cookie](https://github.com/wimglenn/advent-of-code-wim/issues/1) needs to be stored in a file `config.json` in following format:
```
{
    "session_cookie": "your-session-cookie-here"
}
```
An optional parameter `--day` can be passed to force the download for a specific day. Running
```
python path/to/aoc_helper.py --day 5
```
downloads the input file and creates a python script for day 5.

Alternatively, the setup can be run from the powershell script `aoc_setup.ps1` with following syntax:
```
& path/to/aoc_setup.ps1 -day 5
```

## Visualizations

The visualization scripts can be found in `visuals/`.

### Day 7: No Space Left On Device

This script produces a directory tree of the input.

```
📂 /
|------------ 📂 a
|----------------------------- 📂 e
|                |                |---------- 📗 i
|                |---------- 📗 f
|                |---------- 📗 g
|                |------ 📗 h.lst
|------------ 📂 d
|                |---------- 📗 j
|                |------ 📗 d.log
|                |------ 📗 d.ext
|                |---------- 📗 k
|------ 📗 b.txt
|------ 📗 c.dat
```

### Day 12: Hill Climbing Algorithm

Altitudemap of the Jungle

![alt text](https://github.com/danpfister/advent-of-code-2022/blob/main/visuals/12_jungle_map.png?raw=true)
