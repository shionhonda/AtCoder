N, M = map(int, input().split())

left = 1
right = N
for _ in range(M):
    l, r = map(int, input().split())
    left = max(left, l)
    right = min(right, r)
print(max(0, right-left+1))
