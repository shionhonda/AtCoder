N = int(input())

q = []
visited = [0] * N
ans = [0] * N
A = [[] for _ in range(N)]  # tree
W = [[] for _ in range(N)]  # weight

for i in range(N-1):
    u,v,w = map(int, input().split())
    u -= 1
    v -= 1
    A[u].append(v)
    A[v].append(u)
    W[u].append(w)
    W[v].append(w)

q.append(0)  # start
for _ in range(N):
    u = q.pop(0)
    visited[u] = 1
    k = 0
    for v in A[u]:
        if visited[v]==0:
            q.append(v)
            ans[v] = ans[u] + W[u][k]
        k += 1

for a in ans:
    print(a%2)