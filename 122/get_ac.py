N, Q = map(int, input().split())
S = input()

cums = [0 for _ in range(N)]

s0 = None
cum = 0
for i,s in enumerate(S):
    s1 = s
    if s0=="A":
        if s1=="C":
            cum += 1
    s0 = s1
    cums[i] = cum

A = [0 for _ in range(Q)]
for i in range(Q):
    l, r = map(int, input().split())
    A[i] = cums[r-1]-cums[l-1]
for i in range(Q):
    print(A[i])

