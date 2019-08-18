N = int(input())
V = list(map(int, input().split()))

V.sort()
m = V[0]
for v in V[1:]:
    m = (m+v)/2
print(m)