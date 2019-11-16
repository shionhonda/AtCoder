N = int(input())
S = input()

s1 = S[:N//2]
s2 = S[N//2:]
if s1==s2:
    print('Yes')
else:
    print('No')