import lib.aoc as aoc
import re


#-------------------------------------------------------------------------------    
@aoc.main('06', 1)
def main_p1(indata: str) -> str:
    n = 4
    for i in range(len(indata)):
        if len(set(indata[i:i+n])) == n:
            return i+n

#-------------------------------------------------------------------------------    
@aoc.main('06', 2)
def main_p2(indata: str) -> str:
    n = 14
    for i in range(len(indata)):
        if len(set(indata[i:i+n])) == n:
            return i+n

if __name__ == "__main__":
    main_p1()
    main_p2()