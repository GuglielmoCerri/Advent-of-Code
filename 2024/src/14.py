import re
from lib.aoc import aoc

def parse_input(data):
    robots = []
    for line in data:
        match = re.match(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)", line)
        if match:
            px, py, vx, vy = map(int, match.groups())
            robots.append(((px, py), (vx, vy)))
    return robots

def simulate_motion(robots, width, height, steps):
    positions = []
    for (px, py), (vx, vy) in robots:
        x = (px + vx * steps) % width
        y = (py + vy * steps) % height
        positions.append((x, y))
    return positions

def count_quadrants(positions, width, height):
    mid_x, mid_y = width // 2, height // 2
    quadrants = [0, 0, 0, 0]
    for x, y in positions:
        if x == mid_x or y == mid_y:
            continue
        if x < mid_x and y < mid_y:
            quadrants[0] += 1
        elif x >= mid_x and y < mid_y:
            quadrants[1] += 1
        elif x < mid_x and y >= mid_y:
            quadrants[2] += 1
        elif x >= mid_x and y >= mid_y:
            quadrants[3] += 1
    return quadrants

@aoc(14, 2024, 1)
def p1(indata: str) -> int:
    data = indata.strip().splitlines()
    robots = parse_input(data)
    width, height = 101, 103
    steps = 100

    positions = simulate_motion(robots, width, height, steps)
    quadrants = count_quadrants(positions, width, height)
    safety_factor = 1
    for count in quadrants:
        safety_factor *= count

    return safety_factor

@aoc(14, 2024, 2)
def p2(indata: str) -> int:
    data = indata.strip().splitlines()
    robots = parse_input(data)
    width, height = 101, 103  

    t = 0

    while True:
        t += 1
        positions = set()
        valid = True
        
        for (px, py), (vx, vy) in robots:
            x = (px + t * (vx + width)) % width
            y = (py + t * (vy + height)) % height
            if (x, y) in positions:  
                valid = False
                break
            positions.add((x, y))

        if valid:
            return t 


if __name__ == "__main__":
    p1()
    p2()
