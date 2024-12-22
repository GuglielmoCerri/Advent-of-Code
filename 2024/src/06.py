from lib.aoc import aoc

@aoc(6, 2024, 1)
def p1(indata: str) -> int:
    ls = indata.strip().split("\n")
    board = {i + 1j * j: x for i, l in enumerate(ls) for j, x in enumerate(l)}

    start = next(w for w, x in board.items() if x == "^")  
    walls = {w for w, x in board.items() if x == "#"}  
    seen = set()  # Positions visited by the guard

    # Simulate the guard's movement
    z = start
    dz = -1  
    while z in board: 
        seen.add(z)  # Mark current position as visited
        if z + dz in walls:  
            dz *= -1j 
            continue
        z += dz  # Move forward

    return len(seen)


@aoc(6, 2024, 2)
def p2(indata: str) -> int:
    ls = indata.strip().split("\n")
    board = {i + 1j * j: x for i, l in enumerate(ls) for j, x in enumerate(l)}
    start = next(w for w, x in board.items() if x == "^") 
    walls = {w for w, x in board.items() if x == "#"} 

    def causes_loop(obstruction):
        new_walls = walls | {obstruction}  
        z = start
        dz = -1
        seen = set()

        while z in board:
            if (z, dz) in seen:  
                return True
            seen.add((z, dz))
            if z + dz in new_walls: 
                dz *= -1j  
                continue
            z += dz 
        return False

    seen = set()
    z = start
    dz = -1
    while z in board:
        seen.add(z)
        if z + dz in walls:
            dz *= -1j
            continue
        z += dz

    return sum(causes_loop(pos) for pos in seen)


if __name__ == "__main__":
    p1()
    p2()
