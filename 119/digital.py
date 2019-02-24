N = int(input())
X, U = [None]*N, [None]*N
for i in range(N):
    x, u = input().split()
    X[i], U[i] = float(x), u

s = 0
r = 380000.0
for x, u in zip(X, U):
    if u == 'JPY':
        s += x
    else:
        s+= x*r
print(s)