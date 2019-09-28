N, M = map(int, input().split())
AC = []
for _ in range(M):
    a, b = map(int, input().split())
    c_list = list(map(int, input().split()))
    AC.append([a, c_list])

AC = sorted(AC, key=lambda x:x[0])
dp = [10**9]*2**N # Nの有無の全組み合わせ
dp[0] = 0
for m in range(M):
    a, c_list = AC[m]
    c_bi = 0
    for c in c_list:
        c_bi += 2**(c-1)
    for i in range(2**N):
        # dp[i|c_bi]: iからコストaで行ける場所
        dp[i|c_bi] = min(dp[i|c_bi], dp[i]+a) 

ans = dp[-1]
if ans > 10**8:
    print(-1)
else:
    print(dp[-1])