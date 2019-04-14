S = input()
N = len(S)

zeros = [0,0] # even, odd
flg = 0
for s in S:
    if s=='0':
        zeros[flg] += 1
    flg = (flg+1)%2

ones = [(N+1)//2-zeros[0], N//2-zeros[1]]
ans = min(zeros[0]+ones[1], zeros[1]+ones[0])
print(ans)