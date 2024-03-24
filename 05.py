#!/usr/bin/env python3
from sys import stdin
import re

def lines(xs):
    (a,b,c,d) = xs
    if   a==c: return [(a,x) for x in range(min(b,d),max(b,d)+1)]
    elif b==d: return [(x,b) for x in range(min(a,c),max(a,c)+1)]
    return []

def diags(xs):
    (a,b,c,d) = xs
    if (a==c or b==d): return []
    dx, dy = 1 if a < c else -1, 1 if b < d else -1
    l = max(abs(c - a), abs(d - b))
    return [(a + i*dx, b + i*dy) for i in range(l+1)]

ls    = (l.strip() for l in stdin.readlines())
ls    = [tuple(map(int,re.findall(r'\d+',l))) for l in ls]
ms    = [max(col) for col in zip(*ls)]
xm,ym = (max(ms[0],ms[2]), max(ms[1],ms[3]))
arr   = [[0] * (ym+1) for i in range(xm+1)]

for a,b in sum(map(lines, ls),[]): arr[b][a]+=1
p1    = sum(1 for _ in filter(lambda x: x>1, sum(arr,[])))

for a,b in sum(map(diags, ls),[]): arr[b][a]+=1
p2    = sum(1 for _ in filter(lambda x: x>1, sum(arr,[])))

print (f"Part 1: { p1 }, Part 2: { p2 }")
