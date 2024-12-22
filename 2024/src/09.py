from lib.aoc import aoc

def decompress(data):
    map = []
    j = 0
    for i, x in enumerate(data):
        if i % 2 == 0:
            map.extend([j] * int(x))  
            j += 1
        else:
            map.extend(['.'] * int(x))
    return map

def checksum(map):
    res = 0
    for pos, val in enumerate(map):
        if val != '.':
            res += pos * val
    return res

def compact_blocks(map):
    l, r = 0, len(map) - 1
    while l < r:
        if map[l] == '.':
            while map[r] == '.':
                r -= 1
            map[l] = map[r]
            map[r] = '.'
        l += 1
    return map

def compact_files(ns):
    blocks = []
    head = 0
    for i, n in enumerate(ns):
        if not i % 2:
            blocks.append((i // 2, head, head + n))  
        head += n

    for to_move in range(i // 2, -1, -1):  
        block = next(b for b in blocks if b[0] == to_move)  
        _, start, end = block  
        space_needed = end - start  
        
        for i, ((_, _, end1), (_, start2, _)) in enumerate(zip(blocks, blocks[1:])):
            if end1 == end:
                break
            if start2 - end1 >= space_needed:
                blocks.insert(i + 1, (to_move, end1, end1 + space_needed))  
                break
                
    checksum = sum(
        block_id * index
        for block_id, start, end in blocks
        for index in range(start, end)
    )
    return checksum

@aoc(9, 2024, 1)
def p1(indata: str) -> int:
    map = decompress(indata)
    compacted_map = compact_blocks(map)
    return checksum(compacted_map)

@aoc(9, 2024, 2)
def p2(indata: str) -> int:
    ns = list(map(int, indata.strip()))  
    return compact_files(ns)

if __name__ == "__main__":
    p1()
    p2()
