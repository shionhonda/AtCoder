N, W = map(int, input().split())
WV = [list(map(int, input().split())) for _ in range(N)]
dp = [10**12]*(1+10**5)
dp[0] = 0
for i in range(N):
    w,v = WV[i]
    for j in range(len(dp)-1, 0, -1):
        if j-v<=0:
            tmp = w
        else:
            tmp = dp[j-v] + w
        dp[j] = min(dp[j], tmp)
ans = 0
for v,w in enumerate(dp):
    if w<=W:
        ans = max(ans, v)
    else:
        break
print(ans)