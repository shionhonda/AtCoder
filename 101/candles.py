N, K = map(int, input().split())
X = list(map(int, input().split()))

L = N-K+1
Y = [10**9]*(L)
for i in range(L):
    a = X[i]
    b = X[i+K-1]
    if a*b<0:
        Y[i] = 2*min(abs(a), abs(b)) + max(abs(a), abs(b))
    else:
        Y[i] = max(abs(a), abs(b))

print(min(Y))