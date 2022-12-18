import lib.aoc as aoc
import itertools
import math
import functools as ft


#-------------------------------------------------------------------------------
def compare(left, right):
    if type(left) == int and type(right) == int: return left - right
    
    for l,r in itertools.zip_longest(left if type(left)==list else [left], right if type(right)==list else [right]):
        if None in (l,r): return -1 if l == None else 1
        if (v := compare(l, r)) != 0: return v
    return 0

#-------------------------------------------------------------------------------    
@aoc.main('13', 1)
def main_p1(indata: str) -> str:
    indata = indata.split('\n')
    indata = [eval(x) for x in indata if x]

    return sum([i+1 for i in range(len(indata)//2) if compare(*indata[i*2:i*2+2]) < 0])


#-------------------------------------------------------------------------------    
@aoc.main('13', 2)
def main_p2(indata: str) -> str:
    indata = indata.split('\n')
    indata = [eval(x) for x in indata if x]

    return math.prod([i+1 for i,p in enumerate(sorted([[[2]],[[6]]]+indata, key=ft.cmp_to_key(compare))) if p in [[[2]],[[6]]]])


if __name__ == "__main__":
    main_p1()
    main_p2()