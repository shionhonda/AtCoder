N, K = map(int, input().split())
H = list(map(int, input().split()))
MAX = 10**9
dp = [MAX]*N
dp[0] = 0
for i in range(0,N):
    for j in range(1,K+1):
        if i+j>=N:
            break
        tmp = dp[i] + abs(H[i+j]-H[i])
        dp[i+j] = min(dp[i+j], tmp)
print(dp[-1])