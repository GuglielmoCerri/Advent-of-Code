import lib.aoc as aoc
from typing import Tuple
import re


#-------------------------------------------------------------------------------
def split_indata(indata):
    indata = indata.split('\n')
    split = indata.index('') 
    
    return indata[:split].reverse(), indata[split+1:]

#-------------------------------------------------------------------------------    
@aoc.main('05', 1)
def main_p1(indata: str) -> Tuple[int, int]:
    
    items, moves = split_indata(indata)   
    items = [re.findall(r".{1,4}", row) for row in items] # get values for each column
    items = [ [x.strip().replace('[', '').replace(']', '') for x in row] for row in items] # removes extra spaces and [] chars
    cargo = {stack:[] for stack in items[0]}
    
    return 0

#-------------------------------------------------------------------------------    
@aoc.main('05', 2)
def main_p2(indata: str) -> Tuple[int, int]:
    ...

if __name__ == "__main__":
    main_p1()