N = int(input())
deg = [0]*N
edges = [None]*(N-1)
for i in range(N-1):
    a, b = map(int, input().split())
    deg[a-1] += 1
    deg[b-1] += 1
    edges[i] = [a-1,b-1]
C = list(map(int, input().split()))

def sort_with_key(target, key):
    arg = sorted(range(len(key)), key=key.__getitem__)
    return [target[a] for a in arg]

c_sorted = sort_with_key(C, deg)
ans = 0
for a,b in edges:
    ans += min(c_sorted[a], c_sorted[b])
print(ans)
print(' '.join(map(str, c_sorted)))