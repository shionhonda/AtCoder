N, M, C = map(int, input().split())
B = list(map(int, input().split()))
As = [ list(map(int, input().split())) for _ in range(N) ]

cnt = 0
for A in As:
    s = 0
    for a,b in zip(A,B):
        s += a*b
    if s+C>0:
        cnt += 1

print(cnt)