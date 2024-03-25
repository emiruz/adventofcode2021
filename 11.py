#!/usr/bin/env python3
from sys import stdin
from itertools import product, takewhile

clip = lambda x,y: 0 if x>y else x
ps   = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
rs   = map(str.strip, stdin.readlines())
rs   = list(map(lambda r: list(map(int,r)), rs))
n, m = len(rs), len(rs[0])
adj  = lambda i,j: ((i+a,j+b) for a,b in ps if n>a+i>=0 and m>b+j>=0)
idx  = list(product(range(n),range(m)))
cnt  = lambda x: sum([x[i][j]==0 for i,j in idx])

def flood(X, vs):
    if vs==[]:
        for i,j in idx: X[i][j] = clip(X[i][j], 9)
        return X
    (i,j), tail = vs[0], vs[1:]
    if X[i][j] > 9: return flood(X, tail)
    X[i][j] += 1
    if X[i][j] > 9: tail += [(a,b) for a,b in adj(i,j)]
    return flood(X, tail)

p1 = sum(cnt(flood(rs, idx)) for _ in range(100))
p2 = takewhile(lambda x: x, iter(lambda: cnt(flood(rs,idx))!=m*n, object()))

print(f"Part 1: { p1 }, Part 2: { 101 + sum(p2) }")
