from lib.aoc import aoc

def get_score(_map, i, j):
    rows, cols = len(_map), len(_map[0])
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    endpoints = []
    queue = [(i, j)]

    while queue:
        y, x = queue.pop(0)
        curr = _map[y][x]
        _next = curr + 1
        for dy, dx in dirs:
            ny, nx = y + dy, x + dx
            if 0 <= ny < rows and 0 <= nx < cols and _map[ny][nx] == _next:
                if _next == 9:
                    endpoints.append((ny, nx))
                else:
                    queue.append((ny, nx))

    return endpoints

@aoc(10, 2024, 1)
def p1(indata: str) -> int:
    data = indata.strip().splitlines()
    _map = [list(map(int, line)) for line in data]
    rows, cols = len(_map), len(_map[0])

    score = 0
    for i in range(rows):
        for j in range(cols):
            if _map[i][j] == 0:
                endpoints = get_score(_map, i, j)
                score += len(set(endpoints))
    return score

@aoc(10, 2024, 2)
def p2(indata: str) -> int:
    data = indata.strip().splitlines()
    _map = [list(map(int, line)) for line in data]
    rows, cols = len(_map), len(_map[0])

    score = 0
    for i in range(rows):
        for j in range(cols):
            if _map[i][j] == 0:
                endpoints = get_score(_map, i, j)
                score += len(endpoints)
    return score


if __name__ == "__main__":
    p1()
    p2()
