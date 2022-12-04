import lib.aoc as aoc
from typing import Tuple

@aoc.main('01', 1)
def main1(indata: str) -> Tuple[int, int]:
    total_calories = []
    elve_calorie = []

    for i in indata.split('\n'):
        if i:
            elve_calorie.append( int(i) )
        else:
            total_calories.append(elve_calorie)
            elve_calorie = []
            
    calories = [sum(i) for i in total_calories]

    return calories[0]


@aoc.main('01', 2)
def main2(indata: str) -> Tuple[int, int]:
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

    return sum(calories[:3])

if __name__ == "__main__":
    main1()
    main2()