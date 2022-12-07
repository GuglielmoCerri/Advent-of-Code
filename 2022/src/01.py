import lib.aoc as aoc

@aoc.main('01', 1)
def main_p1(indata: str) -> int:
    
    elv_calories = [ sum([int(cal) for cal in calories.split('\n')]) for calories in indata.split('\n\n')]
    elv_calories.sort(reverse=True)

    return elv_calories[0]


@aoc.main('01', 2)
def main_p2(indata: str) -> int:
    elv_calories = [ sum([int(cal) for cal in calories.split('\n')]) for calories in indata.split('\n\n')]
    elv_calories.sort(reverse=True)

    return sum(elv_calories[:3])

if __name__ == "__main__":
    main_p1()
    main_p2()