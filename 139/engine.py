N = int(input())

X = [0]*N
Y = [0]*N
for i in range(N):
    x, y = map(int, input().split())
    X[i] = x
    Y[i] = y

def dot(A, B):
    return A[0]*B[0] + A[1]*B[1]

def dist(d):
    P = [0, 0]
    for i in range(N):
        if dot(d, [X[i], Y[i]])>=0:
            P[0] += X[i]
            P[1] += Y[i]
    return (P[0]**2 + P[1]**2)**0.5

ans = 0
for j in range(N):
    ans = max(ans, dist([X[j], Y[j]]))
print(ans)