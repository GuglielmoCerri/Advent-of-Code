import re
from lib.aoc import aoc


def parse_data(data, part2=False):
    a_match = re.search(r"X\+(\d+), Y\+(\d+)", data[0])
    Ax, Ay = int(a_match.group(1)), int(a_match.group(2))
    
    b_match = re.search(r"X\+(\d+), Y\+(\d+)", data[1])
    Bx, By = int(b_match.group(1)), int(b_match.group(2))
    
    p_match = re.search(r"X=(\d+), Y=(\d+)", data[2])
    Px, Py = int(p_match.group(1)), int(p_match.group(2))
    
    if part2:
        Px += 10000000000000
        Py += 10000000000000
    
    return Ax, Ay, Bx, By, Px, Py

def solve(Ax, Ay, Bx, By, Px, Py):
    """Can be solved using Cramer's rule"""
    # determinant
    det = Ax * By - Ay * Bx
    if det == 0:
        return None
    
    # Cramer's rule
    det_x = Px * By - Py * Bx
    det_y = Ax * Py - Ay * Px
    
    # A e B must be int
    if det_x % det != 0 or det_y % det != 0:
        return None
    
    A = det_x // det
    B = det_y // det
    
    return A * 3 + B * 1

@aoc(13, 2024, 1)
def p1(indata: str) -> int:
    input = [line for line in indata.strip().splitlines() if line]
    grouped = [input[i:i + 3] for i in range(0, len(input), 3)]
    
    total_cost = 0
    for data in grouped:
        Ax, Ay, Bx, By, Px, Py =  parse_data(data)
        cost = solve(Ax, Ay, Bx, By, Px, Py)
        if cost is not None:
            total_cost += cost

    return total_cost

@aoc(13, 2024, 2)
def p2(indata: str) -> int:
    input = [line for line in indata.strip().splitlines() if line]
    grouped = [input[i:i + 3] for i in range(0, len(input), 3)]
    
    total_cost = 0
    for data in grouped:
        Ax, Ay, Bx, By, Px, Py =  parse_data(data, part2=True)
        cost = solve(Ax, Ay, Bx, By, Px, Py)
        if cost is not None:
            total_cost += cost

    return total_cost

if __name__ == "__main__":
    p1()
    p2()