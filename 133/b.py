def euclid(A, B):
    c2 = 0
    for a,b in zip(A,B):
        c2 += (a-b)**2
    return c2**0.5

N, D = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(N)]

cnt = 0
for i in range(N):
    for j in range(i+1,N):
        c = euclid(X[i], X[j])
        if c.is_integer():
            cnt += 1
print(cnt)