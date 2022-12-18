import lib.aoc as aoc
from collections import defaultdict
from itertools import product


ROCKS = [[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 1]],
         [[0, 0, 0, 0], [0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0]],
         [[0, 0, 0, 0], [0, 0, 1, 0], [0, 0, 1, 0], [1, 1, 1, 0]],
         [[1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0]],
         [[0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 0, 0], [1, 1, 0, 0]]]

#-------------------------------------------------------------------------------
def can_move(G, idx, x, y, dx, dy):
    x, y = x + dx, y + dy
    for r, c in product(range(4), repeat = 2):
        if ROCKS[idx][r][c]:
            tmp_x, tmp_y = x + c, y + (3 - r)
            if tmp_y <= 0 or tmp_x <= 0 or tmp_x > 7 or G[tmp_x, tmp_y]: return False
    return (x, y)

#-------------------------------------------------------------------------------    
@aoc.main('17', 1)
def main_p1(indata: str) -> str:
    G = defaultdict(int)
    height, j_idx = 0, 0
    for i in range(2022):
        x, y, ticks = 3, height + 4, 0

        while True:
            if ticks % 2:
                if can_move(G, i%len(ROCKS), x, y, 0, -1): y -= 1
                else: break
            else:
                d = (1, 0) if indata[j_idx%len(indata)] == '>' else (-1, 0)
                res = can_move(G, i%len(ROCKS), x, y, *d)
                if res: x, y = res
                j_idx += 1
            ticks += 1
        
        for r, c in product(range(4), repeat = 2):
            if ROCKS[i%len(ROCKS)][r][c]:
                tmp_x, tmp_y = x + c, y + (3 - r)
                G[tmp_x, tmp_y] = 1
                height = max(height, tmp_y)

    return height

#-------------------------------------------------------------------------------    
@aoc.main('17', 2)
def main_p2(indata: str) -> str:
    G = defaultdict(int)
    found_cycle = False
    Rows, States = defaultdict(set), dict()
    height, j_idx, inc = [0]*3
    tot_ROCKS, i = 1000000000000, -1

    while (i := i + 1) < tot_ROCKS:
        x, y, ticks = 3, height + 4, 0

        while True:
            if ticks % 2:
                if can_move(G, i%len(ROCKS), x, y, 0, -1): y -= 1
                else: break
            else:
                d = (1, 0) if indata[j_idx%len(indata)] == '>' else (-1, 0)
                res = can_move(G, i%len(ROCKS), x, y, *d)
                if res: x, y = res
                j_idx += 1
            ticks += 1

        for r, c in product(range(4), repeat = 2):
            if ROCKS[i%len(ROCKS)][r][c]:
                tmp_x, tmp_y = x + c, y + (3 - r)
                G[tmp_x, tmp_y] = 1
                Rows[tmp_y].add(tmp_x)
                height = max(height, tmp_y)
        
        Hash = (tuple(tuple(sorted(Rows[height - i])) for i in range(32) if height - i >= 0), \
                i % len(ROCKS), j_idx % len(indata))
        if not found_cycle:
            if Hash in States:
                num_ROCKS = i - States[Hash][0]
                num_cycles = (tot_ROCKS - i)//num_ROCKS
                tot_ROCKS -= num_ROCKS*num_cycles
                inc, found_cycle = (height - States[Hash][1])*num_cycles, True
            else: States[Hash] = (i, height)

    return (height + inc)


if __name__ == "__main__":
    main_p1()
    main_p2()
    