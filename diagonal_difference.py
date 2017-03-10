#!/bin/python

import sys


n = int(raw_input().strip())
diff = 0
for i in xrange(n):
    a = raw_input().split()
    diff += (int(a[i]) - int(a[n-1-i]))
print abs(diff)
