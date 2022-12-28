import lib.aoc as aoc

#-----------------------------------------------------------------------------------------------
def decrypt(times, data):
    for orig,n in data*times: 
        data.pop(current := data.index((orig, n)))
        data.insert((current + n) % len(data), (orig, n))
    return sum(data[([n for _,n in data].index(0) + offset) % len(data)][1] for offset in [1000, 2000, 3000])

#-----------------------------------------------------------------------------------------------    
@aoc.main('20', 1)
def main_p1(indata: str) -> str:
    data = [(i,int(line)) for i,line in enumerate(indata.split())]
    return decrypt(1, data.copy())

#-----------------------------------------------------------------------------------------------    
@aoc.main('20', 2)
def main_p2(indata: str) -> str:
    data = [(i,int(line)) for i,line in enumerate(indata.split())]
    return decrypt(10, [(i,n*811589153) for i,n in data])

if __name__ == "__main__":
    main_p1()
    main_p2()