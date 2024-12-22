from lib.aoc import aoc

def is_safe(vals):
    is_inc = all(vals[i] <= vals[i + 1] for i in range(len(vals) - 1))
    is_dec = all(vals[i] >= vals[i + 1] for i in range(len(vals) - 1))
    valid_diff = all(1 <= abs(vals[i] - vals[i + 1]) <= 3 for i in range(len(vals) - 1))
    return (is_inc or is_dec) and valid_diff

@aoc(2, 2024, 1)
def p1(indata: str) -> int:
    res = 0
    for line in indata.splitlines():
        vals = list(map(int, line.split()))  # Converti i valori in interi
        
        if is_safe(vals):
            res += 1
            continue

    return res

@aoc(2, 2024, 2)
def p2(indata: str) -> int:
    res = 0
    for line in indata.splitlines():
        vals = list(map(int, line.split()))  

        if is_safe(vals):
            res += 1
            continue
        
        # Prova a rimuovere ciascun elemento e controlla se diventa "safe"
        for i in range(len(vals)):
            new_vals = vals[:i] + vals[i + 1:]  
            if is_safe(new_vals):
                res += 1
                break 

    return res

if __name__ == "__main__":
   p1()
   p2()