N, W = map(int, input().split())
WV = [list(map(int, input().split())) for _ in range(N)]
dp = [0]*(1+W)
w,v = WV[0]
dp[w:] = [v]*(W+1-w)
for i in range(1,N):
    w,v = WV[i]
    for j in range(W, w-1, -1):
        tmp = dp[j-w] + v
        dp[j] = max(dp[j], tmp)
print(max(dp))