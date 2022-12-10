import lib.aoc as aoc
from collections import defaultdict


#-------------------------------------------------------------------------------
def h_movement(direction:str, h_pos:list) -> list:
    match direction:
        case 'R': h_pos[1] += 1
        case 'L': h_pos[1] -= 1
        case 'U': h_pos[0] -= 1
        case 'D': h_pos[0] += 1
    return h_pos

#-------------------------------------------------------------------------------
def t_movement(h_pos:list, t_pos:list, ph_pos:list) -> list:
    x,y = t_pos
    neighbors = [(x,y),(x+1,y+1),(x-1,y-1),(x+1,y),(x,y+1),(x-1,y),(x,y-1),(x+1,y-1),(x-1,y+1)]
    return t_pos if tuple(h_pos) in neighbors else ph_pos

#-------------------------------------------------------------------------------    
@aoc.main('09', 1)
def main_p1(indata: str) -> int:
    
    indata = indata.split('\n')
    h_pos  = [0,0]
    ph_pos = [0,0] # storing previous last position visited by Head
    t_pos  = [0,0]
    pos_visited = defaultdict(int)

    for move in indata:
        direction, steps = move.split()
        
        for _ in range(int(steps)):
            ph_pos = h_pos[:]
            h_pos = h_movement(direction, h_pos)
            t_pos = t_movement(h_pos, t_pos, ph_pos) 
            pos_visited[ tuple(t_pos) ] += 1
    
    return len(pos_visited)

#-------------------------------------------------------------------------------    
@aoc.main('09', 2)
def main_p2(indata: str) -> str:
    indata = indata.split('\n')

    def move(data):
        x = y = 0
        for move in data:
            direction, steps = move.split()
            for _ in range(int(steps)):
                x += (direction == 'R') - (direction == 'L')
                y += (direction == 'U') - (direction == 'D')
                yield x, y

    def follow(head):
        x = y = 0
        for hx, hy in head:
            if abs(hx - x) > 1 or abs(hy - y) > 1:
                y += (hy > y) - (hy < y)
                x += (hx > x) - (hx < x)
            yield x, y

    tenth = list(follow(move(indata)))

    for _ in range(8):
        tenth = follow(tenth)

    return len(set(tenth))

if __name__ == "__main__":
    main_p1()
    main_p2()