import lib.aoc as aoc
from typing import Tuple

@aoc.main('01')
def main(indata: str) -> Tuple[int, int]:
    total_calories = []
    elve_calorie = []

    for i in indata.split('\n'):
        if i:
            elve_calorie.append( int(i) )
        else:
            total_calories.append(elve_calorie)
            elve_calorie = []
            
    calories = [sum(i) for i in total_calories]
    calories.sort(reverse=True)

    return calories[0], sum(calories[:3])

if __name__ == "__main__":
    main()