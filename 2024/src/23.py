from itertools import combinations
import networkx as nx

from lib.aoc import aoc


@aoc(23, 2024, 1)
def p1(indata):
    G = nx.Graph()
    for line in indata.splitlines():
        parts = line.split("-")
        G.add_edge(parts[0], parts[1])

    cliques = [c for c in nx.find_cliques(G) if len(c) >= 3 and any(n[0] == "t" for n in c)]
    sets = set()
    for c in cliques:
        for nodes in combinations(c, 3):
            if any(n[0] == "t" for n in nodes):
                sets.add(tuple(sorted(nodes)))
    count = len(sets)

    return count
    

@aoc(23, 2024, 2)
def p2(indata):
    G = nx.Graph()
    for line in indata.splitlines():
        parts = line.split("-")
        G.add_edge(parts[0], parts[1])

    cliques = nx.find_cliques(G)
    LAN = sorted(sorted(cliques, key=len, reverse=True)[0])

    return ",".join(LAN)

if __name__ == "__main__":   
    p1()
    p2()
