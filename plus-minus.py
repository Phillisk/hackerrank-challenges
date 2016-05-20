"""
	Given an array of integers, calculate which fraction of its elements are positive, 
	which fraction of its elements are negative, and which fraction of its elements are zeroes, 
	respectively. Print the decimal value of each fraction on a new line.
	Input Format

		The first line contains an integer, N, denoting the size of the array. 
		The second line contains N space-separated integers describing an array of numbers[a1,a2,a3,....an-1,an].

	Output Format

		You must print the following 3 lines:

		A decimal representing of the fraction of positive numbers in the array.
		A decimal representing of the fraction of negative numbers in the array.
		A decimal representing of the fraction of zeroes in the array."""
#!/bin/python

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
pos,neg,zero = 0.0,0.0,0.0
for i in arr:
    if i > 0:
        pos += 1
    elif i < 0:
        neg += 1
    else:
        zero += 1

print round(pos/n,6)
print round(neg/n,6)
print round(zero/n,6)

     
