"""
Roy wanted to increase his typing speed for programming contests. 
So, his friend advised him to type the sentence 
"The quick brown fox jumps over the lazy dog" repeatedly, because it is a pangram. 
(Pangrams are sentences constructed by using every letter of the alphabet at least once.)

Given a sentence , tell Roy if it is a pangram or not.

Input Format

Input consists of a string s.

Constraints 
Length of s can be at most  1000 and atleast 1 and it may contain spaces, lower case and upper case letters. Lower-case and upper-case instances of a letter are considered the same.

Output Format

Output a line containing pangram if s is a pangram, otherwise output not pangram.
"""
import sys

def pangram(s):
    s = s.upper()
    alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
    l = len(s)
    if l >= 1 and l <= 1000:
        i = 1
        
        while l >= 0:
            exists = s.find(alphabets[i-1:i])
            if exists == -1:
                return "not pangram"
            else:
                i = i+1
                l = l-1
        return "pangram"

print pangram(raw_input())