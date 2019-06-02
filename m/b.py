S = input()

cnt = 0
for s in S:
    if s=='o':
        cnt += 1
cnt += 15-len(S)
if cnt>=8:
    print('YES')
else:
    print('NO')