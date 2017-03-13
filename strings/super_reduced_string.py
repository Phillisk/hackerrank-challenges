# Enter your code here. Read input from STDIN. Print output to STDOUT

S0 = str(raw_input())
S1 = list(S0)

i = 0

while i < len(S1)-1:
    if S1[i] == S1[i+1]:
        del S1[i]
        del S1[i]
        i = 0
        if len(S1) == 0:
            print 'Empty String'
            break
    else: 
        i += 1
    
print ''.join(S1)
