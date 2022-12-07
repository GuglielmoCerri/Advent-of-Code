import lib.aoc as aoc
from typing import Tuple

score_dict  = { 'X':1, 'Y':2, 'Z':3}
choose_dict = { 'A':'X', 'B':'Y', 'C':'Z' }
game = { 
    ('X','Y') : 6,
    ('X','Z') : 0,
    ('Y','X') : 0,
    ('Y','Z') : 6,
    ('Z','X') : 6,
    ('Z','Y') : 0,
    ('X','X') : 3,
    ('Y','Y') : 3,
    ('Z','Z') : 3,
}

lose = { 
    'X' : 'Z',
    'Y' : 'X',
    'Z' : 'Y'
}

win = {
    'X' : 'Y',
    'Y' : 'Z',
    'Z' : 'X'
}

@aoc.main('02', 1)
def main_p1(indata: str) -> int:
    data = indata.split('\n')
    score = 0

    for i in data:
        c1, c2 = i.split()
        c1 = choose_dict[c1]

        score += 3 if c1 == c2 else game[ (c1, c2) ]
        score += score_dict[c2]

    return score

@aoc.main('02', 2)
def main_p2(indata: str) -> int:
    data = indata.split('\n')
    score = 0

    for i in data:
        c1, c2 = i.split()
        c1 = choose_dict[c1]

        match c2:
            case 'X':
                c3 = lose[c1]
            case 'Y':
                c3 = c1    
            case 'Z':
                c3 = win[c1]

        score += score_dict[c3] + game[ (c1, c3) ]

    return score

if __name__ == "__main__":
    main_p1()
    main_p2()