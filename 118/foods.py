N,M = map(int, input().split())
foods = [0]*M
for i in range(N):
    tmp = list(map(int, input().split()))
    for f in tmp[1:]:
        foods[f-1] += 1
cnt = 0
for i in range(1,M+1):
    if foods[i-1]==N:
        cnt += 1
print(cnt)
