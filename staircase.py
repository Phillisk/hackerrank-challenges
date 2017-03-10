#!/bin/python

import sys


n = int(raw_input().strip())
x = ' '
y = '#'
for i in range(1,n+1):
    print x * int(n-i) + y * int(i)
