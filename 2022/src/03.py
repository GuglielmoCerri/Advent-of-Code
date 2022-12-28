import lib.aoc as aoc
from typing import Tuple
import string

ALPHABET = list(string.ascii_lowercase)


@aoc.main('03', 1)
def main_p1(indata: str) -> int:
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
def main_p2(indata: str) -> int:
    data = indata.split('\n')
    score = 0

    for i in range(0, len(data), 3):
        s1,s2,s3 = data[i:i+3]
        common = set(s1) & set(s2) & set(s3)
        common = next(iter(common))
        val = ALPHABET.index(common.lower()) + 1
        if common.isupper():
            score += val + 26
        else:
            score += val
        
    return score

if __name__ == "__main__":
    main_p1()
    main_p2()