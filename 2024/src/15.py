from lib.aoc import aoc

dirs = {
        "^": (-1, 0),
        "v": (1, 0),
        "<": (0, -1),
        ">": (0, 1),
    }

def get_robot_pos( grid):
    rows, cols = len(grid), len(grid[0])
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "@":
                return (i, j)

def moving( grid, pos, moves, part):
    for move in moves:
        """
        # zip looks nice but way too slow
        ny, nx = (a + b for a, b in zip(pos, dirs[move]))
        """
        ny = pos[0] + dirs[move][0]
        nx = pos[1] + dirs[move][1]

        if grid[ny][nx] == ".":
            pos = (ny, nx)
        elif grid[ny][nx] == "#":
            continue
        else:
            edges, adjs = get_adjs_and_edges(grid, pos, move, part)
            blocked = 0
            dy, dx = dirs[move]
            for box in edges:
                ny, nx = (box[0] + dy, box[1] + dx)
                if grid[ny][nx] == "#":
                    blocked += 1
            if blocked == 0:
                grid = update_grid(grid, adjs, move)
                pos = (pos[0] + dy, pos[1] + dx)
    return grid

def get_adjs_and_edges( grid, pos, move, part=1):
    y, x = pos
    dy, dx = dirs[move]

    adjs = set()
    if part == 1 or move in "<>":
        while True:
            ny, nx = y + dy, x + dx
            if grid[ny][nx] in ".#":
                return [(ny - dy, nx - dx)], adjs
            y = ny
            x = nx
            adjs.add((y, x))
    else:
        edges = []
        queue = [(y, x)]
        while queue:
            y, x = queue.pop(0)
            if (y, x) in adjs:
                continue
            adjs.add((y, x))
            ny, nx = y + dy, x + dx
            if grid[ny][nx] in ".#":
                edges.append((y, x))
            elif grid[ny][nx] == "[":
                queue.append((ny, nx))
                queue.append((ny, nx + 1))
            elif grid[ny][nx] == "]":
                queue.append((ny, nx))
                queue.append((ny, nx - 1))

        return edges, adjs - {(pos[0], pos[1])}

def update_grid( grid, adjs, move):
    sorted_coords = []

    # sort coords from the edge to the robot's position
    match move:
        case "^":
            sorted_coords = sorted(adjs, key=lambda x: x[0])
        case "v":
            sorted_coords = sorted(adjs, key=lambda x: x[0], reverse=True)
        case "<":
            sorted_coords = sorted(adjs, key=lambda x: x[1])
        case ">":
            sorted_coords = sorted(adjs, key=lambda x: x[1], reverse=True)

    dy, dx = dirs[move]
    for coord in sorted_coords:
        y, x = coord
        ny, nx = y + dy, x + dx
        grid[ny][nx] = grid[y][x]
        grid[y][x] = "."

    return grid

def get_coords_sum( grid, part=1):
    box = "[" if part == 2 else "O"
    rows, cols = len(grid), len(grid[0])
    _sum = sum(100 * y + x for y in range(rows) for x in range(cols) if grid[y][x] == box)
    return _sum

def resize_grid( grid):
    _mappings = {
        "#": "##",
        "O": "[]",
        ".": "..",
        "@": "@.",
    }
    new_grid = [list("".join(_mappings[c] for c in line)) for line in grid]
    return new_grid

@aoc('15', 1)
def p1(indata: str):
    part = 1
    grid, moves = indata.split("\n\n")
    grid = [list(row) for row in grid.split("\n")]
    moves = list("".join(moves.split("\n")))

    pos = get_robot_pos(grid)
    grid[pos[0]][pos[1]] = "."

    grid = moving(grid, pos, moves, part)
    _sum = get_coords_sum(grid, part)
    return _sum

@aoc('15', 2)
def p2(indata: str):
    part = 2
    grid, moves = indata.split("\n\n")
    grid = [list(row) for row in grid.split("\n")]
    moves = list("".join(moves.split("\n")))

    grid = resize_grid(grid)

    pos = get_robot_pos(grid)
    grid[pos[0]][pos[1]] = "."

    grid = moving(grid, pos, moves, part)
    _sum = get_coords_sum(grid, part)
    return _sum


if __name__ == "__main__":
    p1()
    p2()
