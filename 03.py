#!/usr/bin/env python3
from statistics import mode, mean
from sys import stdin

def f(ls0, i=0,flip=False):
    if len(ls0) == 1: return ls0[0]
    v  = '0' if mean([int(r[i]) for r in ls0]) < 0.5 else '1'
    if flip: v = '0' if v=='1' else '1'
    return f([ls0[j] for j,x in enumerate(ls0) if x[i]==v], i+1, flip)

ls  = [l.strip() for l in stdin]
p1  = zip(*(l for l in ls))
p1  = int("".join((mode(col) for col in p1)),2)
p1 *= ~p1 & 0b111111111111 # Mask corresponds to input width.
p2  = int(f(ls,flip=False),2) * int(f(ls,flip=True),2)

print(f"Part 1: { p1 }, Part 2: { p2 } ")
