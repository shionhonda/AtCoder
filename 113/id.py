import numpy as np

N,M = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(M)]
order = [[] for _ in range(N)]
for p,y in X:
    order[p-1].append(y)
    
for i in range(N):
    order[i] = np.argsort(np.argsort(order[i]))
cnts = [0 for _ in range(N)]
for i in range(M):
    p = X[i][0]
    print('{:06}{:06}'.format(p, order[p-1][cnts[p-1]]+1) )
    cnts[p-1] += 1