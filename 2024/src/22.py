from collections import defaultdict

from lib.aoc import aoc

@aoc(22, 2024, 1)
def p1(indata):
    res = []
    for n in map(int, indata.splitlines()):
        for _ in range(2000):
            n = ( (n * 64) ^ n ) % 16777216 
            n = ( (n // 32) ^ n ) % 16777216 
            n = ( (n * 2048) ^ n ) % 16777216 
        res.append(n)
    return sum(res)

@aoc(22, 2024, 2)
def p2(indata):
    prices = []
    for n in map(int, indata.splitlines()):
        price = []
        for _ in range(2000):
            n = ( (n * 64) ^ n ) % 16777216 
            n = ( (n // 32) ^ n ) % 16777216 
            n = ( (n * 2048) ^ n ) % 16777216
            price.append(n % 10) 
        prices.append(price)
    
    changes = [[b - a for a, b in zip(p, p[1:])] for p in prices]
    amounts = defaultdict(int)
    for buyer_idx, change in enumerate(changes):
        keys = set()
        for i in range(len(change) - 3):
            key = tuple(change[i : i + 4])
            if key in keys:
                continue
            amounts[key] += prices[buyer_idx][i + 4]
            keys.add(key)
    max_amount = max(amounts.values())

    return max_amount

if __name__ == "__main__":   
    p1()
    p2()
