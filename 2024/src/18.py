from lib.aoc import aoc
import networkx as ntx

USE_NETWORKX = False
GRID = None
GRAPH = None
SIZE = None
CORRUPTED = None
CORRUPTED_LENGTH = None


def parse_data(data):
    global CORRUPTED, SIZE, CORRUPTED_LENGTH, GRID
    CORRUPTED = [[*map(int, line.split(","))] for line in data]

    SIZE = 71
    CORRUPTED_LENGTH = 1024

    if len(CORRUPTED) == 25:  # test input
        SIZE = 7
        CORRUPTED_LENGTH = 12

    set_grid()


def set_grid():
    global GRID, GRAPH
    GRID = [["."] * SIZE for _ in range(SIZE)]
    for x, y in CORRUPTED[:CORRUPTED_LENGTH]:
        GRID[y][x] = "#"

    if USE_NETWORKX:
        GRAPH = ntx.Graph()
        for y in range(SIZE):
            for x in range(SIZE):
                if GRID[y][x] == ".":
                    GRAPH.add_node((x, y))
                    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < SIZE and 0 <= ny < SIZE and GRID[ny][nx] == ".":
                            GRAPH.add_edge((x, y), (nx, ny))


def add_corrupted(cx, cy):
    global GRID, GRAPH
    if GRID is not None:
        GRID[cy][cx] = "#"

    if USE_NETWORKX and GRAPH is not None:
        GRAPH.remove_node((cx, cy))


def get_shortest_path_steps():
    size = len(GRID)

    start = (0, 0)
    end = (size - 1, size - 1)

    if USE_NETWORKX:
        try:
            path = ntx.shortest_path(GRAPH, start, end)
            return len(path) - 1
        except ntx.exception.NetworkXNoPath:
            return -1
    else:
        # BFS
        queue = [(start, 0)]  
        seen = set()
        while queue:
            pos, length = queue.pop(0)
            if pos == end:
                return length
            if pos in seen:
                continue
            seen.add(pos)
            x, y = pos
            for dx, dy in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < size and 0 <= ny < size and GRID[ny][nx] == ".":
                    queue.append(((nx, ny), length + 1))
        return -1  # no path

@aoc(18, 2024, 1)
def p1(indata):
    global USE_NETWORKX
    USE_NETWORKX = False
    data = indata.strip().splitlines()
    parse_data(data)
    steps = get_shortest_path_steps()
    return steps

@aoc(18, 2024, 2)
def p2(indata):
    global USE_NETWORKX, CORRUPTED_LENGTH
    USE_NETWORKX = False
    data = indata.strip().splitlines()
    parse_data(data)

    start = CORRUPTED_LENGTH
    end = len(CORRUPTED)

    while end - start > 1:
        mid = (start + end) // 2
        CORRUPTED_LENGTH = mid
        set_grid()
        steps = get_shortest_path_steps()
        if steps == -1:
            end = mid
        else:
            start = mid

    return f"{CORRUPTED[end - 1][0]},{CORRUPTED[end - 1][1]}"


if __name__ == "__main__":
    p1()
    p2()
