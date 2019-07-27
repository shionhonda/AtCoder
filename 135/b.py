N = int(input())
P = list(map(int, input().split()))
Q = list(range(1,N+1))

cnt = 0
for p,q in zip(P,Q):
    if p!=q:
        cnt += 1

if cnt <=2:
    print('YES')
else:
    print('NO')