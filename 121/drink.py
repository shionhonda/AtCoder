import numpy as np

N, M = map(int, input().split())

AB = [ list(map(int, input().split())) for _ in range(N) ]
AB = np.array(AB)
AB = AB[AB[:,0].argsort(), :]

m = 0
s = 0
for n in range(N):
    s += AB[n][0]*AB[n][1]
    m += AB[n][1]
    if m>=M:
        s -= AB[n][0]*(m-M)
        break
print(s)
        

        