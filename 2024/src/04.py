from lib.aoc import aoc

def find_xmas(grid):
    def check_direction(x, y, dx, dy):
        word = ""
        for i in range(4):
            nx, ny = x + i * dx, y + i * dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                word += grid[nx][ny]
            else:
                return False
        return word == "XMAS"

    directions = [
        (0, 1),  
        (0, -1),  
        (1, 0), 
        (-1, 0),  
        (1, 1), 
        (-1, -1), 
        (1, -1),
        (-1, 1), 
    ]

    count = 0
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            for dx, dy in directions:
                if check_direction(x, y, dx, dy):
                    count += 1
    return count

def find_xmas_x(grid):
    rows, cols = len(grid), len(grid[0])
    count = 0

    _set = {"M", "S"}

    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            if grid[r][c] == "A":
                top_left_bottom_right = {grid[r - 1][c - 1], grid[r + 1][c + 1]}  # top-left to bottom-right diagonal
                top_right_bottom_left = {grid[r - 1][c + 1], grid[r + 1][c - 1]}  # top-right to bottom-left diagonal
                
                if top_left_bottom_right == _set and top_right_bottom_left == _set:
                    count += 1
    return count

@aoc(4, 2024, 1)
def p1(indata: str) -> int:
    grid = [list(row) for row in indata.splitlines()]
    return find_xmas(grid)

@aoc(4, 2024, 2)
def p2(indata: str) -> int:
    grid = [list(row) for row in indata.splitlines()]
    return find_xmas_x(grid)

if __name__ == "__main__":
    p1()
    p2()
