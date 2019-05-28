import math 

N, M = map(int, input().split())
S = []
for _ in range(M):
    S.append(list(map(int, input().split()[1:])))
P = list(map(int, input().split()))

ans = 0
for i in range(2**N):
    i_bin = bin(i)[2:]
    i_bin = (N - len(i_bin))*'0' + i_bin
    flag = True
    for m in range(M):
        cnt = 0
        for n in range(N):
            if i_bin[n]=='1' and n+1 in S[m]:
                cnt += 1
        if cnt%2 != P[m]:
            flag = False
            break
    if flag:
        ans += 1

print(ans)