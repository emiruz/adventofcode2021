#!/usr/bin/env python3
from itertools import takewhile, dropwhile, accumulate
from functools import reduce
from sys import stdin

def board():
    if stdin.readline() == '': return None
    g  = lambda xs: map(int, filter(None, xs.split()))
    return [list(g(x)) for x in (stdin.readline() for _ in range(5))]

trans  = lambda xs: list(map(list, zip(*xs)))
chk_   = lambda b: any(all(r) for r in b) or any(all(r) for r in trans(b))
chk    = lambda bs: any((chk_(b) for b in bs))
ns     = [int(n) for n in stdin.readline().strip().split(",")]
bs     = list(takewhile(lambda x: x, iter(board, object())))
init   = [[[False]*5 for _ in range(5)] for _ in range(len(bs))]
pick   = lambda ii,n,i,j,k: True if bs[i][j][k] == n else ii[i][j][k]
play   = lambda x,n: ([[[pick(x[0],n,i,j,k) for k in range(5)]
                       for j in range(5)] for i in range(len(x[0]))],n)
scor   = lambda p,i: sum(x for v,x in zip(sum(p,[]), sum(bs[i],[])) if not v)
state  = list(accumulate(ns, play, initial=(init,None)))
stats  = sum([[(b,i,n) for i,b in enumerate(s) if chk_(b)] for s,n in state],[])
p1,i,n = stats[0]
last   = reduce(lambda a,x: a if len(a)==1 else [y for y in a if y!=x[1]],
                stats, list(range(len(bs))))[0]
p2,j,m = next(filter(lambda x: x[1] == last, stats))

print (f"Part 1: { scor(p1,i)*n }, Part 2: { scor(p2,j)*m }")
