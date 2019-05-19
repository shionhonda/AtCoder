import math
N, K = map(int, input().split())

ans = 0
for i in range(1,N+1):
    if i>=K:
        t = 1
    else:
        t = (1/2)**( math.ceil( math.log2(K/i)))
    ans += t / N

print(ans)