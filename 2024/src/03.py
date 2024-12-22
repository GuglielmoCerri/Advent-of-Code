from lib.aoc import aoc
import re

def find_instructions(data):
    """Extract valid mul(X,Y) instructions."""
    pattern = r'mul\(\d{1,3},\d{1,3}\)'
    return re.findall(pattern, data)

def find_int_from_instructions(instructions):
    """Extract integers from mul instructions."""
    data = []
    for ins in instructions:
        data.append(tuple(map(int, re.findall(r'\d{1,3}', ins))))
    return data   

@aoc(3, 2024, 1)
def p1(indata: str) -> int:
    instructions = find_instructions(indata)
    vals = find_int_from_instructions(instructions)
    return sum(x * y for x, y in vals)

@aoc(3, 2024, 2)
def p2(indata: str) -> int:
    """Solution for Part 2."""
    pattern = r"(mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\))"
    enabled = True  # mul instructions are enabled by default
    result = 0

    for match in re.finditer(pattern, indata):
        instruction = match.group(0)

        if instruction == "do()":
            enabled = True
        elif instruction == "don't()":
            enabled = False
        elif instruction.startswith("mul") and enabled:
            x, y = map(int, re.findall(r'\d{1,3}', instruction))
            result += x * y

    return result

if __name__ == "__main__":
    p1()
    p2()
