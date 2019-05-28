N, K = map(int, input().split())
V = list(map(int, input().split()))

ans = -10**9
R = min(N, K)
A = R
for a in range(0, A+1):
    B = R-a
    for b in range(0, B+1):
        if b>0:
            v = V[:a] + V[-b:]
        else:
            v = V[:a]
        
        v.sort()
        
        cnt = 0
        for vv in v:
            if vv<0:
                cnt += 1
            else:
                break
        ans = max(ans, sum(v[min(K-a-b, cnt):]))
        
print(ans)