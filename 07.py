#!/usr/bin/env python3
from sys import stdin

xs   = list(map(int, stdin.read().strip().split(',')))
sums = lambda x: x * (x+1) // 2
fit1 = lambda i: sum(map(lambda x: abs(x-i), xs))
fit2 = lambda i: sum(map(lambda x: sums(abs(x-i)), xs))
scr  = lambda f: [(f(i),i) for i in range(min(xs), max(xs)+1)]
p1   = min(map(lambda x: x[0], scr(fit1)))
p2   = min(map(lambda x: x[0], scr(fit2)))

print (f"Part 1: { p1 }, Part 2: { p2 }")
