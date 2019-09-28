N, M = map(int, input().split())
AC = []
for _ in range(M):
    a, b = map(int, input().split())
    c_list = list(map(int, input().split()))
    AC.append([a, sorted(c_list)])

AC = sorted(AC, key=lambda x:x[0])
print(AC)
dp = [10**7]*M
for m in M:
    a, c_list = AC[m]
    for i in range(m-1,-1,-1):
        a_tmp, c_list_tmp = AC[m-1]
        flg = True
        for c in c_list_tmp:
            if c not in c_list:
                flg = False
                break
        if flg:
            dp[m] = min(dp[m-1], )
