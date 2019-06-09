N = int(input())
W = list(map(int, input().split()))

S1 = sum(W)
S2 = 0
ans = 10**4
for w in W:
    S1 -= w
    S2 += w
    ans = min(ans, abs(S1-S2))

print(ans)