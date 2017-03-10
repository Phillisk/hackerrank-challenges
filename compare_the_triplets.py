#!/bin/python

import sys


a0,a1,a2 = raw_input().strip().split(' ')
a0,a1,a2 = [int(a0),int(a1),int(a2)]
b0,b1,b2 = raw_input().strip().split(' ')
b0,b1,b2 = [int(b0),int(b1),int(b2)]

A1 = 0
B1 = 0

for i, j in zip([a0, a1, a2],[b0, b1, b2]):
    if i > j:
        A1 += 1
    elif i < j:
        B1 += 1
    else:
        pass
            
print A1, B1
