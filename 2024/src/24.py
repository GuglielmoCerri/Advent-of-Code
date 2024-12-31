from collections import defaultdict

from lib.aoc import aoc


@aoc(24, 2024, 1)
def p1(indata):
    A, B = indata.split('\n\n')
    
    a = {}
    for l in A.splitlines():
        v, x = l.split(': ')
        a[v] = int(x)
    
    ind = {}
    g = defaultdict(list)
    d = {}
    
    for l in B.splitlines():
        u, o, v, _, w = l.split()
        g[u].append(w)
        g[v].append(w)
        op = dict(zip(['AND', 'OR', 'XOR'], [int.__and__, int.__or__, int.__xor__]))[o]
        d[w] = (u, v, op)
        ind[w] = 2
    
    s = list(a.keys())
    while s:
        w = s.pop()
        if w in d:
            u, v, o = d[w]
            a[w] = o(a[u], a[v])
        for adj in g[w]:
            ind[adj] -= 1
            if ind[adj] == 0:
                s.append(adj)
    
    i = 0
    k = f'z{i:02}'
    ans = 0
    while k in a:
        ans += a[k] << i
        i += 1
        k = f'z{i:02}'
    
    return ans

@aoc(24, 2024, 2)
def p2(indata):
    A, B = indata.split('\n\n')
    
    a = {}
    for l in A.splitlines():
        v, x = l.split(': ')
        a[v] = int(x)
    
    ind = {}
    g = defaultdict(list)
    d = {}
    
    for l in B.splitlines():
        u, o, v, _, w = l.split()
        g[u].append(w)
        g[v].append(w)
        op = dict(zip(['AND', 'OR', 'XOR'], [int.__and__, int.__or__, int.__xor__]))[o]
        d[w] = (u, v, op)
        ind[w] = 2
    
    s = list(a.keys())
    while s:
        w = s.pop()
        if w in d:
            u, v, o = d[w]
            a[w] = o(a[u], a[v])
        for adj in g[w]:
            ind[adj] -= 1
            if ind[adj] == 0:
                s.append(adj)
    
    i = 0
    k = f'z{i:02}'
    ans = 0
    while k in a:
        ans += a[k] << i
        i += 1
        k = f'z{i:02}'
    
    s = []
    
    def f(w, b):
        if not b: 
            s.append(w)
    
    for w, (u, v, o) in d.items():
        if w[0] == 'z':
            f(w, o is int.__xor__ and (u[0] not in 'xy' or w == 'z00') or w == 'z45')
        elif d[g[w][0]][2] == int.__or__:
            f(w, o is int.__and__)
        else:
            f(w, o is int.__or__ or o is int.__xor__ and u[0] in 'xy' and u[1:] > '00' or o is int.__and__ and u in ('x00', 'y00'))
    
    return ','.join(sorted(s))

if __name__ == "__main__":   
    p1()
    p2()
