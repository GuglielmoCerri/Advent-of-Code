import lib.aoc as aoc
import re


#-------------------------------------------------------------------------------
def split_indata(indata):
    indata = indata.split('\n')
    split = indata.index('') 
    
    return indata[:split], indata[split+1:]

#-------------------------------------------------------------------------------    
@aoc.main('05', 1)
def main_p1(indata: str) -> str:
    
    items, moves = split_indata(indata)   
    items.reverse()
    items = [re.findall(r".{1,4}", row) for row in items] # get values for each column
    items = [ [x.strip().replace('[', '').replace(']', '') for x in row] for row in items] # removes extra spaces and [] chars
    crates = [ {idx+1:crate for idx, crate in enumerate(item) if crate} for item in items[1:] ]

    cargo = {int(stack):[] for stack in items[0]}
    for i in crates:
        for c in i:
            cargo[c].append(i[c])

    for move in moves:
        n, origin, end = [int(d) for d in re.findall(r'\d+',move)]
        cargo[end].extend( [cargo[origin].pop() for _ in range(n)] )

    return ''.join([cargo[k][-1] for k in cargo.keys()])

#-------------------------------------------------------------------------------    
@aoc.main('05', 2)
def main_p2(indata: str) -> str:
    
    items, moves = split_indata(indata)   
    items.reverse()
    items = [re.findall(r".{1,4}", row) for row in items] # get values for each column
    items = [ [x.strip().replace('[', '').replace(']', '') for x in row] for row in items] # removes extra spaces and [] chars
    crates = [ {idx+1:crate for idx, crate in enumerate(item) if crate} for item in items[1:] ]

    cargo = {int(stack):[] for stack in items[0]}
    for i in crates:
        for c in i:
            cargo[c].append(i[c])

    for move in moves:
        n, origin, end = [int(d) for d in re.findall(r'\d+',move)]
        cargo[end].extend(cargo[origin][-n:])
        del cargo[origin][-n:]  

    return ''.join([cargo[k][-1] for k in cargo.keys()])

if __name__ == "__main__":
    main_p1()
    main_p2()