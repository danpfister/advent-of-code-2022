# Advent of Code 2022
-----
Solving the [Advent of Code 2022](https://adventofcode.com/2022) with Python 3.10 (and some C++14)

## AOC Downloader

The `aoc_downloader.py` can be used to create a folder and download the input for a specific day.

### Usage

The [session cookie](https://github.com/wimglenn/advent-of-code-wim/issues/1) needs to be stored in a file `config.json` in this format:

```
{
    "session_cookie": "your-session-cookie-here"
}
```

Running `python path/to/aoc_downloader.py` creates a directory with the input file inside.

Passing the optional parameter `--day` or `--year` forces the download for a specific date, otherwise it defaults to the current date (The month is always assumed to be December).
The optional parameter `--py` adds an empty python file to the created directory.

For example, running

```
python path/to/aoc_downloader.py --day 17 --year 2021 --py
```

creates the folder and files as follows:

```
advent-of-code/
|
|-- day17/
|     |
|     |-- input.txt
|     |-- day17.py
|
|-- aoc_downloader.py

```

## Visualizations

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

### Day 8: Treetop Tree House

Visible trees:

![alt text](https://github.com/danpfister/advent-of-code-2022/blob/main/visuals/08_visible_trees.png?raw=true)

### Day 12: Hill Climbing Algorithm

Heightmap of the jungle

![alt text](https://github.com/danpfister/advent-of-code-2022/blob/main/visuals/12_jungle_map.png?raw=true)
