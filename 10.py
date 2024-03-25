#!/usr/bin/env python3
from sys import stdin
from statistics import median

pos, neg = '([{<', ')]}>'
ps1, ps2 = {')':3,']':57,'}':1197,'>':25137}, {')':1,']':2,'}':3,'>':4}

def P (xs,es=[]):
    if len(xs)==0: return (None, es)
    e, x, c = None if not es else es[0], xs[0], neg[pos.find(xs[0])]
    if e is None: return x if x in neg else P(xs[1:],[c])
    if x in pos:  return P(xs[1:], [c]+es)
    elif x != e:  return (x,es)
    else:         return P(xs[1:], es[1:])

scr = lambda xs, s=0: s if not xs else scr(xs[1:], 5*s+ps2.get(xs[0]))
ls  = list(map(str.strip, stdin.readlines()))
p1  = sum(map(lambda x: ps1.get(x[0]), filter(lambda x: x[0], list(map(P, ls)))))
p2  = median(map(lambda x: scr(x[1]), filter(lambda x: not x[0], map(P, ls))))

print(f"Part 1: { p1 }, Part 2: { p2 }")
