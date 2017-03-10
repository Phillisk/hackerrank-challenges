#!/bin/python

import sys


a,b,c,d,e = raw_input().strip().split(' ')
A1 = [int(a),int(b),int(c),int(d),int(e)]

min = 0
max = 0

A2 = sorted(A1)
A3 = sorted(A1, key=int, reverse=True)

del A2[-1]
del A3[-1]

for i in A2:
    min += i
for j in A3:
    max += j
    
print min, max
