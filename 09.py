#!/usr/bin/env python3
from sys import stdin
from math import prod
from itertools import product

ps   = [(0,-1),(0,1),(-1,0),(1,0)]
rs   = list(map(lambda x: list(map(int, x.strip())), stdin.readlines()))
n,m  = len(rs), len(rs[0])
adj  = lambda i,j: ((a+i,b+j) for a,b in ps if n>a+i>=0 and m>b+j>=0)
v    = lambda i,j: rs[i][j]
comp = lambda i,j: all([v(i,j) < v(a,b) for a,b in adj(i,j)])
lps  = [(i,j) for i,j in product(range(n),range(m)) if comp(i,j)]
B_   = lambda i,j: [(a,b) for a,b in adj(i,j) if v(i,j)<v(a,b) and v(a,b)<9]
Br   = lambda i,j: sum((Br(a,b) for a,b in B_(i,j)),[]) + B_(i,j)
B    = lambda i,j: list(set(Br(i,j)+[(i,j)]))
p1   = sum(1+v(i,j) for i,j in lps)
p2   = sorted(map(lambda x: len(B(*x)), lps))

print (f"Part 1: { p1 }, Part 2: { prod(p2[-3:]) }")
