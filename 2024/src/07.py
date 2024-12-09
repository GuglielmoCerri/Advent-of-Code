import re

from lib.aoc import aoc

def check(test, vals, part2=False):    
    test = int(test)
    
    def h(test, vals, i, res):
        if i == len(vals):
            return res == test
        
        next_val = vals[i]
        return (
            h(test, vals, i + 1, res + next_val) or
            h(test, vals, i + 1, res * next_val) or
            (h(test, vals, i + 1, int(str(res) + str(next_val))) if part2 else False)
        )
        
    return h(test, vals, 1, vals[0])
    

@aoc('07', 1)
def p1(indata: str) -> int:
    res = 0
    for data in indata.splitlines():
        test, rest = data.split(":")
        vals = list(map(int, re.findall(r'\d{1,3}', rest)))
        if check(test, vals):
            res += int(test) 
    return res


@aoc('07', 2)
def p2(indata: str) -> int:
    res = 0
    for data in indata.splitlines():
        test, rest = data.split(":")
        vals = list(map(int, re.findall(r'\d{1,3}', rest)))
        if check(test, vals, part2=True):
            res += int(test) 
    return res


if __name__ == "__main__":
    p1()
    p2()
