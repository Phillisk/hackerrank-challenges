#!/bin/python

import sys


s = raw_input().strip()

i = 1

for j in s:
    if j.isupper():
        i += 1
    else:
        pass
print i
        
