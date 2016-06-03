# Enter your code here. Read input from STDIN. Print output to STDOUT

T = int(raw_input().strip())


def palindrome_index(word):
    
    X = len(word)
    while X <= 100000 + 5 and X >= 1:
        if word == word[::-1]:
            return -1
        else:
            if word[1] == word[-1]:
                return 0
            else:
                return X - 1
for i in range(T):
    if 1 <= T <= 20:
        word = raw_input().strip()
        print palindrome_index(word)