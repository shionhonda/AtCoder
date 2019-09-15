N, K, Q = map(int, input().split())
A = [int(input()) for _ in range(Q)]

pts = [K-Q]*N
for a in A:
    pts[a-1] +=1
for p in pts:
    if p>0:
        print('Yes')
    else:
        print('No')
