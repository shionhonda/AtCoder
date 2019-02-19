S = input() # string
K = int(input())

n = 0 # First index of a number that is not equal to 1
for s in S:
    if s=='1':
        n += 1
    else:
        break

if K-1<n:
    print('1')
else:
    print(s)