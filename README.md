# Advent-of-Code
![Github last commit](https://img.shields.io/github/last-commit/GuglielmoCerri/Advent-of-Code)
[![python](https://img.shields.io/badge/python-v3-blue)](https://www.python.org/)

## Introduction
[Advent of Code](https://adventofcode.com/2022/about) is an Advent calendar of small programming puzzles for a variety of skill sets and skill levels that can be solved in any programming language you like.

This repository contains the complete solutions to AoC 2021 and 2022 in python

In total I currently have 100 ⭐. 

In this repo you will find the solutions to:
*   AoC 2021 in jupyter notebook 
*   AoC 2022 in python3.10

## Installation

Create the environment from the environment.yml file inside the specific year folder:

```bash
> cd <year> # cd 2024
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

From 2024, you can use the Python package [`aocd`](https://github.com/wimglenn/advent-of-code-data) to automatically download the inputs for the various quizzes. You just need to create a `.env` file inside `src/lib` that contains the variable `AOC_SESSION` with the session token of the account you are logged in with on Advent of Code, as the inputs are different for each user.

The session ID is a cookie which is set when you login to AoC. You can find it with your browser inspector. If you need help with that part then you can look [here](https://github.com/wimglenn/advent-of-code-wim/issues/1).

It is also possible to run all days, at once, within a year using: 

```bash
> python3 run_all.py
```

## Solutions
Here is a list of the Advent of Code years for which I have provided solutions:

- [Year 2021](https://github.com/GuglielmoCerri/Advent-of-Code/tree/main/2021)
- [Year 2022](https://github.com/GuglielmoCerri/Advent-of-Code/tree/main/2022)
- [Year 2024](https://github.com/GuglielmoCerri/Advent-of-Code/tree/main/2024)

Feel free to explore each year to see how I approached various problems!

## Contributions
I'm proud to announce that my solutions have been integrated into the [awesome-advent-of-code](https://github.com/Bogdanp/awesome-advent-of-code) repository. This curated repository compiles the best Advent of Code resources, including language-specific sections.

To directly navigate to the Python section where my solutions reside, you can [click here](https://github.com/Bogdanp/awesome-advent-of-code#python).

Thank you for exploring my Advent of Code journey. I hope you find these solutions insightful and enjoyable!

---

## License

Distributed under the MIT License. See [LICENSE](./LICENSE) for more information.


## Contact

Guglielmo Cerri - cerriguglielmo@gmail.com

Project Link: [https://github.com/GuglielmoCerri/Advent-of-Code](https://github.com/GuglielmoCerri/Advent-of-Code)


