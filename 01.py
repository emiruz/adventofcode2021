#!/usr/bin/env python3
from sys import stdin

ls   = [int(l.strip()) for l in stdin]
cnt  = sum([a < b for a,b in zip(ls[:-1], ls[1:])])
ws   = [a+b+c for a,b,c in zip(ls[:-2], ls[1:-1], ls[2:])]
cnt2 = sum([a < b for a,b in zip(ws[:-1], ws[1:])])

print (f"Part 1: {cnt}, Part 2: {cnt2}")
