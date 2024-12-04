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

@aoc('04', 1)
def p1(indata: str) -> int:
    grid = [list(row) for row in indata.splitlines()]
    return find_xmas(grid)

@aoc('04', 2)
def p2(indata: str) -> int:
    ...

if __name__ == "__main__":
    p1()
    p2()
