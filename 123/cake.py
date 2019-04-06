x, y, z, N = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A.sort(reverse=True)
B.sort(reverse=True)
C.sort(reverse=True)

Q = [[0,0,0]]
i,j,k = Q[0]
P = [A[i]+B[j]+C[k]]

def next(P,Q, cnt):
    if len(P)<0 or cnt==N:
        return
    print(P, Q)
    p = P.pop(0)
    print(p)
    i,j,k = Q.pop(0)
    if i+1<x:
        P.append(A[i+1] + B[j] + C[k])
        Q.append([i+1,j,k])
    if j+1<y:
        P.append(A[i] + B[j+1] + C[k])
        Q.append([i,j+1,k])
    if k+1<z:
        P.append(A[i] + B[j] + C[k+1])
        Q.append([i,j,k+1])
    ids = sorted(range(len(P)), key=lambda k:P[k], reverse=True)
    tmp = [Q[id] for id in ids]
    Q = tmp
    P.sort(reverse=True)
    next(P, Q, cnt+1)
        

next(P, Q, 0)