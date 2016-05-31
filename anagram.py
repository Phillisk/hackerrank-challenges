# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(raw_input().strip())

def anagram(S):

    X = len(S)
    S1 = S[:X/2]
    S2 = S[X/2:]
    count = 0

    while 1 <= X <= 10000:
        if X % 2 == 0:
            i = 1
            l = len(S1)
            while l >= 0:
                exists = S2.find(S1[i-1:i])
                if exists == -1:
                    count += 1
                    i = i+1
                    l = l-1
                else:
                    i = i+1
                    l = l-1
            return count
        else:
            return -1

for i in range(T):
    if 1 <= T <= 100:
        S = raw_input().strip()
        print anagram(S)
            
