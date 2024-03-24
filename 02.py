#!/usr/bin/env python3
from functools import reduce, partial
from sys import stdin
from math import prod

look = { "forward": lambda x: (x,0), "up": lambda x: (0,-x), "down": lambda x: (0,x) }
ls   = [(l[0], int(l[1])) for l in (l.strip().split() for l in stdin)]
xs   = [sum(col) for col in zip(*(look.get(k)(x) for k,x in ls))]
look = { "forward": lambda x,a,b,c: (a,    b+x, c+a*x),
         "up":      lambda x,a,b,c: (-x+a, b,   c),
         "down":    lambda x,a,b,c: (x+a,  b,   c) }
ys   = (partial(look.get(k), x) for k,x in ls)
ys   = reduce(lambda a, f: f(*a), ys, (0,0,0))

print (f"Part 1: { prod(xs) }, Part 2: { prod(ys[1:]) }")
