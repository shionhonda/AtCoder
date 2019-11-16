# 解法2
# https://img.atcoder.jp/abc145/editorial.pdf

N, T = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]
AB = [[a,-b] for a,b in AB]
AB = sorted(AB)
AB = [[a,-b] for a,b in AB]
print(AB)

dp = [[0]*(T-1) for _ in range(N+1)]
last = 0
for n in range(N):
    for t in range(T-1):
        A, B = AB[n]
        if t>=A:
            if dp[n][t-A]+B > dp[n][t]:
                dp[n+1][t] = dp[n][t-A]+B
                last = n
            else:
                dp[n+1][t] = dp[n][t]
        else:
            dp[n+1][t] = dp[n][t]

for a in dp:
    print(a)

print(last)

if last==N-1:
    print(dp[N][T-2])
else:
    print(dp[N][T-2]+AB[last+1][1])