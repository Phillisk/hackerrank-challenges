#!/bin/python

import sys


time = raw_input().strip()

period = time[-2:]

if period == "PM":
    hr = int(time[:2])
    if hr != 12:
        hr1 = hr + 12
    else:
        hr1 = 12
    time1 = time[2:-2]
    final = str(hr1)+ time1 
else:
    hr = int(time[:2])
    if hr == 12:   
        hr1 = "00"
        time1 = time[2:-2]
        final = str(hr1)+ time1
    else:
        final = time[:-2]

print final
