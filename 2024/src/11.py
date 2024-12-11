from collections import Counter
from lib.aoc import aoc

def res(values, N):
    stones = Counter(values)

    for _ in range(N):
        new_stones = Counter()

        for stone, count in stones.items():
            if stone == '0':
                new_stones['1'] += count
            elif len(stone) % 2 == 0:
                mid = len(stone) // 2
                left, right = stone[:mid], stone[mid:]
                left = left.lstrip('0') or '0'
                right = right.lstrip('0') or '0'
                new_stones[left] += count
                new_stones[right] += count
            else:
                new_stones[str(int(stone) * 2024)] += count

        stones = new_stones

    return sum(stones.values())

@aoc('11', 1)
def p1(indata: str) -> int:
    values = indata.split()
    return res(values, N = 25)
    

@aoc('11', 2)
def p2(indata: str) -> int:
    values = indata.split()
    return res(values, N = 75)

if __name__ == "__main__":
    p1()
    p2()
