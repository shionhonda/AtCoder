N,M = map(int, input().split())
X = [ [int(j) for j in input().split()] for _ in range(N)]
ans = 0
for i in range(1<<3):
    if M==0:
        break
    ss = [None]*N

    for n in range(0,N):
        x,y,z = X[n]
        s = (x if (i & (1<<2)) else -x) \
            + (y if (i & (1<<1)) else -y) \
            + (z if (i & (1<<0)) else -z)
        ss[n] = s
    ss.sort()
    ans = max(ans, sum(ss[N-M:]))
print(ans)