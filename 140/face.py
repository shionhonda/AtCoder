N, K = map(int, input().split())
S = input()

ans = 0
for i in range(N-1):
    if S[i] == S[i+1]:
        ans += 1

if ((N-1)-ans) < 2*K:
    print(N-1)
else:
    print(ans + 2*K)