import lib.aoc as aoc

#-----------------------------------------------------------------------------------------------
def solve(elves, checks, dif, rnd, prop, part1=True):
    while any(any(elf+dir in elves for dir in [-1j,1-1j,1,1+1j,1j,-1+1j,-1,-1-1j]) for elf in elves):
        for elf in [elf for elf in elves if any(elf+dir in elves for dir in [-1j,1-1j,1,1+1j,1j,-1+1j,-1,-1-1j])]:
            dir = next((check[0] for check in checks if all(elf+dir not in elves for dir in check)), 0)
            if dir!=0: prop={e:d for e,d in prop.items() if d!=dest} if (dest:=elf+dir) in prop.values() else prop | {elf: dest}
        elves, checks, rnd, prop = elves - set(prop.keys()) | set(prop.values()), checks[1:]+[checks[0]], rnd+1, {}
        if rnd-1 == 10 and part1: 
            return dif([c.real for c in elves]) * dif([c.imag for c in elves]) - len(elves)
    
    return rnd

#-----------------------------------------------------------------------------------------------    
@aoc.main('23', 1)
def main_p1(indata: str) -> str:
    data  = indata.split('\n')
    elves = {complex(x,y) for x in range(len(data[0])) for y in range(len(data)) if data[y][x]=='#'}
    checks, dif, rnd, prop = [[-1j,1-1j,-1-1j],[1j,1+1j,-1+1j],[-1,-1-1j,-1+1j],[1,1-1j,1+1j]], lambda nums: int(max(nums)-min(nums))+1, 1, {}
    
    return solve(elves, checks, dif, rnd, prop)

#-----------------------------------------------------------------------------------------------    
@aoc.main('23', 2)
def main_p2(indata: str) -> str:
    elves = {complex(x,y) for x in range(len(indata.split('\n')[0])) for y in range(len(indata.split('\n'))) if indata.split('\n')[y][x]=='#'}
    checks, dif, rnd, prop = [[-1j,1-1j,-1-1j],[1j,1+1j,-1+1j],[-1,-1-1j,-1+1j],[1,1-1j,1+1j]], lambda nums: int(max(nums)-min(nums))+1, 1, {}

    return solve(elves, checks, dif, rnd, prop, part1=False)
    
if __name__ == "__main__":
    main_p1()
    main_p2()