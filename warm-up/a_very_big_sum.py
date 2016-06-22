#!/bin/python

import sys

total  = 0
n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

for i in arr:
    total += i
    i += 1
print total