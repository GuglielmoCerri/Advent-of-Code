import lib.aoc as aoc
from typing import Tuple
import string

ALPHABET = list(string.ascii_lowercase)


@aoc.main('03', 1)
def main1(indata: str) -> Tuple[int, int]:
    data = indata.split('\n')
    score = 0

    for i in data:
        len_ = len(i)
        s1 = i[0: int(len_/2)]
        s2 = i[int(len_/2): len_]
        common = set(s1).intersection(set(s2))
        common = next(iter(common))
        val = ALPHABET.index(common.lower()) + 1
        if common.isupper():
            score += val + 26
        else:
            score += val
        
    return score

@aoc.main('03', 2)
def main2(indata: str) -> Tuple[int, int]:
    data = indata.split('\n')
    score = 0

    for i in data:
        len_ = len(i)
        s1 = i[0: int(len_/2)]
        s2 = i[int(len_/2): len_]
        common = set(s1).intersection(set(s2))
        common = next(iter(common))
        val = ALPHABET.index(common.lower()) + 1
        if common.isupper():
            score += val + 26
        else:
            score += val
        
    return score

if __name__ == "__main__":
    main1()