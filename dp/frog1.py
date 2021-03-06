N = int(input())
H = list(map(int, input().split()))
MAX = 10**9
dp = [MAX]*N
dp[0] = 0
dp[1] = abs(H[1]-H[0])
for i in range(2,N):
    dp1 = dp[i-1]+abs(H[i]-H[i-1])
    dp2 = dp[i-2]+abs(H[i]-H[i-2])
    dp[i] = min(dp1, dp2)
print(dp[-1])