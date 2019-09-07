N = int(input())
P = list(map(int, input().split()))

first, second = 0, 0
ans = 0
for i in range(0, N-1):
    first = max(P[i], P[i+1])
    second = min(P[i], P[i+1])
    ans += second
    if i<N-2:
        for j in range(i+2,N):
            new = P[j]
            if new > first:
                second = first
                first = new
            elif new < first and new > second:
                second = new
            else:
                pass
            ans += second

print(ans)