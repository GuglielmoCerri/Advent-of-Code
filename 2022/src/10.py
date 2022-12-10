import lib.aoc as aoc


#-------------------------------------------------------------------------------    
@aoc.main('10', 1)
def main_p1(indata: str) -> int:
    
    indata = indata.split('\n')
    x = 0
    cycle = 1
    value = 1

    for line in indata:
        if cycle in (20, 60, 100, 140, 180, 220):
            x += cycle * value

        if line.startswith("noop"):
            cycle += 1
        else:

            if cycle + 1 in (20, 60, 100, 140, 180, 220):
                x += (cycle + 1) * value
            cycle += 2
            value += int(line.split()[1])

    return x

#-------------------------------------------------------------------------------    
@aoc.main('10', 2)
def main_p2(indata: str) -> str:
    indata = indata.split('\n')
    msg = ""
    cycle = 1
    value = 1

    for line in indata:
        if (cycle - 1) % 40 == 0:
            msg += "\n"
        msg += "#" if (cycle - 1) % 40 in (value - 1, value, value + 1) else " "
    
        if line.startswith("noop"):
            cycle += 1
        else:
            if cycle % 40 == 0:
                msg += "\n"
            msg += "#" if cycle % 40 in (value - 1, value, value + 1) else " "
            cycle += 2
            value += int(line.split()[1])
            
    return msg

if __name__ == "__main__":
    main_p1()
    main_p2()