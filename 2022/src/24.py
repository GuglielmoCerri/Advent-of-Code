import lib.aoc as aoc
from itertools import product


#-----------------------------------------------------------------------------------------------
def travel(s, e, m, n, D, G, B):
    t, Active = 0, set([s])
    while t := t + 1:
        if e in Active: break
        B = [(d, (2 + ((d[0] + p[0]-2)%(m-2)), 2 + ((d[1] + p[1]-2)%(n-2)))) for d, p in B]
        Possible, Blocked = set(), set(p for _, p in B)

        for dr, p in product(list(D.values()) + [(0, 0)], Active):
            q = tuple(sum(x) for x in zip(p, dr))
            if q not in Blocked and G[q[0]][q[1]] != '#': Possible.add(q)
        Active = Possible
    return B, t - 1

#-----------------------------------------------------------------------------------------------    
@aoc.main('24', 1)
def main_p1(indata: str) -> str:
    L = list(map(lambda x: list(x.strip()), indata.split('\n')))
    m, n = len(L), len(L[0])

    G = [['#']*(n+2)] + [['#'] + l + ['#'] for l in L] + [['#']*(n+2)]
    D = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}
    B = [(D[G[r][c]], (r, c)) for r in range(len(G)) for c in range(len(G[r])) if G[r][c] in {'^', 'v', '<', '>'}]
    start, end = (1, next(i for i, c in enumerate(G[1]) if c == '.')), (m, next(i for i, c in enumerate(G[-2]) if c == '.'))

    t, Active = 0, set([start])
    while t := t + 1:
        if end in Active: break
        B = [(d, (2 + ((d[0] + p[0]-2)%(m-2)), 2 + ((d[1] + p[1]-2)%(n-2)))) for d, p in B]
        Possible, Blocked = set(), set(p for _, p in B)

        for dr, p in product(list(D.values()) + [(0, 0)], Active):
            q = tuple(sum(x) for x in zip(p, dr))
            if q not in Blocked and G[q[0]][q[1]] != '#': Possible.add(q)
        Active = Possible

    return t - 1

#-----------------------------------------------------------------------------------------------    
@aoc.main('24', 2)
def main_p2(indata: str) -> str:
    L = list(map(lambda x: list(x.strip()), indata.split('\n')))
    m, n = len(L), len(L[0])

    G = [['#']*(n+2)] + [['#'] + l + ['#'] for l in L] + [['#']*(n+2)]
    D = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}
    B = [(D[G[r][c]], (r, c)) for r in range(len(G)) for c in range(len(G[r])) if G[r][c] in {'^', 'v', '<', '>'}]
    start, end = (1, next(i for i, c in enumerate(G[1]) if c == '.')), (m, next(i for i, c in enumerate(G[-2]) if c == '.'))
    
    B, t1 = travel(start, end, m, n, D, G, B) 
    B, t2 = travel(end, start, m, n, D, G, B) 
    _, t3 = travel(start, end, m, n, D, G, B)
    
    return t1 + t2 + t3
    
if __name__ == "__main__":
    main_p1()
    main_p2()