N = int(input())
H = [list(map(int, input().split())) for _ in range(N)]
dp = [[0,0,0] for _ in range(N)]
dp[0] = H[0]
for i in range(1,N):
    dp[i][0] = H[i][0] + max(dp[i-1][1], dp[i-1][2])
    dp[i][1] = H[i][1] + max(dp[i-1][2], dp[i-1][0])
    dp[i][2] = H[i][2] + max(dp[i-1][0], dp[i-1][1])
print(max(dp[-1]))