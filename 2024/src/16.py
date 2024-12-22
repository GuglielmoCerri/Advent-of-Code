from lib.aoc import aoc

def find_routes(data):
    grid = []
    start = None
    end = None
    for y, row in enumerate(data):
        grid_row = []
        for x, cell in enumerate(row):
            grid_row.append(cell)
            if cell == "S":
                start = (y, x)
            elif cell == "E":
                end = (y, x)
        grid.append(grid_row)

    dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    routes = []
    visited = {}

    queue = [(start, [start], 0, 0)]  # (y, x), history, score, direction
    while queue:
        (y, x), history, curr_score, curr_dir = queue.pop(0)

        if (y, x) == end:
            routes.append((history, curr_score))
            continue

        """
        if you only want to find the minimun score (e.g. part1),
        you can ignore the tiles where visited[((y, x), curr_dir)] <= curr_score, this will be faster

        however, if you want to find all the possible routes,
        you need to ignore tiles where visited[((y, x), curr_dir)] < curr_score
        this will be slower but fits both parts
        """
        if ((y, x), curr_dir) in visited and visited[((y, x), curr_dir)] < curr_score:
            continue

        visited[((y, x), curr_dir)] = curr_score

        for _dir, (dy, dx) in enumerate(dirs):
            if (curr_dir + 2) % 4 == _dir:
                continue

            ny, nx = y + dy, x + dx
            if grid[ny][nx] != "#" and (ny, nx) not in history:
                if _dir == curr_dir:
                    queue.append(((ny, nx), history + [(ny, nx)], curr_score + 1, _dir))  # move forward
                else:
                    queue.append(((y, x), history, curr_score + 1000, _dir))  # turn

    return routes

@aoc(16, 2024, 1)
def p1(indata: str):
    possible_routes = find_routes(indata.strip().splitlines())
    min_score = min(r[1] for r in possible_routes)
    return min_score

@aoc(16, 2024, 2)
def p2(indata: str):
    possible_routes = find_routes(indata.strip().splitlines())
    min_score = min(r[1] for r in possible_routes)
    best_routes = [r for r in possible_routes if r[1] == min_score]
    tiles = {tile for route in best_routes for tile in route[0]}
    return len(tiles)


if __name__ == "__main__":
    p1()
    p2()
