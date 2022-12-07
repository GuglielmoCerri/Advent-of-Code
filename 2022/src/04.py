import lib.aoc as aoc
from typing import Tuple

#-------------------------------------------------------------------------------      
def range_subset(range1, range2):
    cond1 = range1.start in range2 and range1[-1] in range2
    cond2 = range2.start in range1 and range2[-1] in range1
    return cond1 or cond2

#-------------------------------------------------------------------------------    
def full_range_subset(range1, range2):
    return len(set( list(range1) ).intersection(set( list(range2) ))) > 0


#-------------------------------------------------------------------------------    
@aoc.main('04', 1)
def main_p1(indata: str) -> int:
    data = indata.split('\n')
    dup  = 0
    
    for i in data:
        elv1, elv2 = i.split(',')
        elv1_1, elv1_2 = elv1.split('-')
        elv2_1, elv2_2 = elv2.split('-')
        r1 = range(int(elv1_1), int(elv1_2)+1)
        r2 = range(int(elv2_1), int(elv2_2)+1)
        dup += range_subset(r1, r2)
        
    return dup

#-------------------------------------------------------------------------------    
@aoc.main('04', 2)
def main_p2(indata: str) -> int:
    data = indata.split('\n')
    dup  = 0
    
    for i in data:
        elv1, elv2 = i.split(',')
        elv1_1, elv1_2 = elv1.split('-')
        elv2_1, elv2_2 = elv2.split('-')
        r1 = range(int(elv1_1), int(elv1_2)+1)
        r2 = range(int(elv2_1), int(elv2_2)+1)
        dup += full_range_subset(r1, r2)
        
    return dup

if __name__ == "__main__":
    main_p1()
    main_p2()