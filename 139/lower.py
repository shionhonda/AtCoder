N = int(input())
H = list(map(int, input().split()))

prev = H[0]
ans, cnt = 0, 0
for cur in H[1:]:
    if cur <= prev:
        cnt += 1
    else:
        ans = max(ans, cnt)
        cnt = 0
    prev = cur
ans = max(ans, cnt)
print(ans)