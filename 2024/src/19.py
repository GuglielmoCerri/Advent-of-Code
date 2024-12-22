from lib.aoc import aoc
from collections import defaultdict


def is_valid_design(design, towels):
    def matching_towel(pos):
        if pos == len(design):
            return True

        for towel in towels:
            next_pos = pos + len(towel)
            if next_pos <= len(design) and design[pos:next_pos] == towel:
                if matching_towel(next_pos):
                    return True

        return False

    return matching_towel(0)

def get_valid_count(design, towels):
    cache = defaultdict(int)

    def matching_towel(pos):
        if pos == len(design):
            return 1

        if cache[pos] > 0:
            return cache[pos]

        matches = 0
        for towel in towels:
            next_pos = pos + len(towel)
            if next_pos <= len(design) and design[pos:next_pos] == towel:
                matches += matching_towel(next_pos)

        cache[pos] = matches
        return matches

    return matching_towel(0)

@aoc('19', 1)
def p1(indata):
    data = indata.strip().splitlines()
    towels = sorted(data[0].split(", "), key=len)
    designs = data[2:]

    count = 0
    for design in designs:
        if is_valid_design(design, towels):
            count += 1
    return count

@aoc('19', 2)
def p2(indata):
    data = indata.strip().splitlines()
    towels = sorted(data[0].split(", "), key=len)
    designs = data[2:]

    total = 0
    for design in designs:
        total += get_valid_count(design, towels)
    return total

if __name__ == "__main__":
    p1()
    p2()
