N = int(input())

dp = [10**9] * (N+1)
dp[0], dp[1] = 0, 1
i = 6
while i<=N:
    dp[i] = 1
    i *= 6
i = 9
while i<=N:
    dp[i] = 1
    i *= 9

for i in range(1,N):
    dp[i+1] = min(dp[i+1], dp[i]+1)
    j = 6
    while i+j <= N:
        dp[i+j] = min(dp[i+j], dp[i]+1)
        j *= 6
    j = 9
    while i+j <= N:
        dp[i+j] = min(dp[i+j], dp[i]+1)
        j *= 9

print(dp[N])
