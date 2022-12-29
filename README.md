[![License: MIT](https://img.shields.io/badge/license-MIT-red)](https://github.com/GuglielmoCerri/Advent-of-Code)
![Github last commit](https://img.shields.io/github/last-commit/GuglielmoCerri/Advent-of-Code)
[![python](https://img.shields.io/badge/python-v3.10.8-blue)](https://www.python.org/)

# 🎄 Advent-of-Code 🎅

## Introduction
Advent of Code ([link](https://adventofcode.com/2022/about)) is an Advent calendar of small programming puzzles for a variety of skill sets and skill levels that can be solved in any programming language you like.

This repository contains the complete solutions to AoC 2021 and 2022 in python

In total I currently have 100 ⭐. 

In this repo you will find the solutions to:
*   AoC 2021 in jupyter notebook 
*   AoC 2022 in python3.10

## Installation

Create the environment from the environment.yml file inside the specific year folder:

```bash
> cd <year> # cd 2022
> conda env create -f environment.yml
```

## Usage

To run a single solution:

```bash
> conda activate AoC # Activate conda environment
```

```bash
> python3 src/<DAY>.py
```

At the end of the script is created a `log` file inside the `<year>` folder. 
It will contains the solution and the elapsed time for both part 1 and part 2
for that day.

It is also possible to run all days, at once, within a year using: 

```bash
> python3 run_all.py
```

## License

Distributed under the MIT License. See [LICENSE](./LICENSE) for more information.


## Contact

Guglielmo Cerri - cerriguglielmo@gmail.com

Project Link: [https://github.com/GuglielmoCerri/Advent-of-Code](https://github.com/GuglielmoCerri/Advent-of-Code)


