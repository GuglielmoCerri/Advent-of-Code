from lib.aoc import aoc

@aoc(1, 2024, 1)
def p1(indata: str) -> int:
    
    c1, c2 = [], []
    for line in indata.splitlines():
        vals = line.strip().split()
        c1.append(int(vals[0]))
        c2.append(int(vals[1]))
   
    c1.sort()
    c2.sort()

    return sum([abs(c1[i] - c2[i]) for i in range(len(c1))])


@aoc(1, 2024, 2)
def p2(indata: str) -> int:
    c1, c2 = [], []
    for line in indata.splitlines():
        vals = line.strip().split()
        c1.append(int(vals[0]))
        c2.append(int(vals[1]))

    return sum([v * c2.count(v) for v in c1])

if __name__ == "__main__":
    p1()
    p2()