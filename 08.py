#!/usr/bin/env python3
from sys import stdin
from itertools import permutations as P

chars  = "abcdefg"
nums   = ["abcefg","cf","acdeg","acdfg","bcdf","abdfg","abdefg","acf","abcdefg","abcdfg"]
nums   = list(map(set,nums))
digits = lambda x: [i for i,n in enumerate(nums) if n==set(x)]
t      = lambda x,ii: "".join([chars[ii[chars.find(c)]] for c in x])
rs     = list(map(lambda l: l.replace('| ','').split(), stdin.readlines()))
conv   = lambda p, xs: sum((digits(t(x,p)) for x in xs),[])
find   = lambda xs: next(p for p,i in ((p,len(conv(p,xs))) for p in P([0,1,2,3,4,5,6])) if i==10)
ps     = [conv(p, r[10:]) for r,p in ((r, find(r[0:10])) for r in rs)]
p1     = len(list(filter(lambda x: x in [1,4,7,8], sum(ps,[]))))
p2     = sum(map(lambda x: int("".join(map(str,x))), ps))

print(f"Part 1: { p1 }, Part 2: { p2 }")
