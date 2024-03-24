#!/usr/bin/env python3
from sys import stdin
from functools import reduce

init  = list(map(int, stdin.read().strip().split(',')))
arr   = [0,0,0,0,0,0,0,0,0]
for x in init: arr[x] += 1
tick  = lambda a,b,c,d,e,f,g,h,i: [b,c,d,e,f,g,a+h,i,a]
ticks = lambda m, init: sum (reduce (lambda a,n: tick(*a), range(m), init))

print(f"Part 1: { ticks(80, arr.copy()) }, Part 2: { ticks(256, arr) }")
