#I did this
#!/bin/python

import sys


n = int(raw_input().strip())
height = map(int,raw_input().strip().split(' '))

i = 0
total = 0

for j in height:
    if j > i:
        largest = j
        i += 1
    else:
        largest = i
        i += 1

for j in height:
    if j == largest:
        total += 1
        
print total

#Then I remembered the built in functions and this worked
#!/bin/python

import sys


n = int(raw_input().strip())
height = map(int,raw_input().strip().split(' '))

tallest = max(height)

print height.count(tallest)
