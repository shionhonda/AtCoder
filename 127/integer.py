N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

BC = [list(map(int, input().split())) for _ in range(M)]
BC.sort(key=lambda x:x[1], reverse=True)

s = 0
b,c = BC.pop(0)
for i,a in enumerate(A):
    if b>=1:
        if c > a:
            s += c
            b -= 1
        else:
            s += a
    if b<=0:
        if len(BC)==0:
            s += sum(A[i+1:])
            break
        else:
            b,c = BC.pop(0)

print(s)