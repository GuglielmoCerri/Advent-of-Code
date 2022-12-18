import lib.aoc as aoc

def bfs(grid, width, height, start, target, f):
    queue, visited = [[start]], {start}
    while queue:
        if (p := (path := queue.pop(0))[-1]) == target or grid[(cy := p[1])][(cx := p[0])] == target: return len(path)-1
        for x, y in [(cx-1,cy), (cx,cy-1), (cx+1,cy), (cx,cy+1)]:
            if (x,y) not in visited and 0<=x<width and 0<=y<height and ((ord(grid[y][x]) - ord(grid[cy][cx]))*f <= 1):
                queue, visited = queue + [path + [(x, y)]], visited | {(x, y)}

#-------------------------------------------------------------------------------    
@aoc.main('12', 1)
def main_p1(indata: str) -> str:
    indata = indata.split('\n')
    
    width, height = len(indata[0]), len(indata)
    (start,end), grid = map(lambda c: ((i:=''.join(indata).find(c))%width,i//width),'SE'), \
                                      [l.replace('S','a').replace('E','z') for l in indata]
   
    return bfs(grid, width, height, start, end, 1)

#-------------------------------------------------------------------------------    
@aoc.main('12', 2)
def main_p2(indata: str) -> str:
    indata = indata.split('\n')
    
    width, height = len(indata[0]), len(indata)
    (start,end), grid = map(lambda c: ((i:=''.join(indata).find(c))%width,i//width),'SE'), \
                                      [l.replace('S','a').replace('E','z') for l in indata]
   
    return bfs(grid, width, height, end, 'a', -1)


if __name__ == "__main__":
    main_p1()
    main_p2()