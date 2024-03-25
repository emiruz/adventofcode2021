#!/usr/bin/env python3
from sys import stdin
from itertools import groupby
from functools import reduce

ls = list(map(str.strip, stdin.readlines()))
ls = list(map(lambda x: x.split('-'), ls))
ls = sorted(ls + list(map(lambda x: x[::-1], ls)))
ls = groupby(ls, key=lambda x: x[0])
ls = dict(map(lambda x: (x[0], list(map(lambda y: y[1],x[1]))),ls))

def dfs(x, f, xs=["start"], vs=[]):
    if x == "end": return [xs]
    if x.islower() and not x=="start": vs = [x] + vs
    nxt = [l for l in ls[x] if l != "start" and \
           not (l!="end" and f(l, vs))]
    return sum([dfs(x, f, xs+[x], vs) for x in nxt],[])

def cond(x, vs):
    y = groupby(sorted(filter(str.islower, [x] + vs)))
    y = list(map(lambda x: len(list(x[1])), y))
    if y == []: return False
    return max(y) > 2 or sum(map(lambda x: x>1, y))>1

p1 = len(dfs("start", lambda x,vs: x in vs))
p2 = len(dfs("start", cond))

print(f"Part 1: { p1 }, Part 2: { p2 }")
