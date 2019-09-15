import heapq

N, M = map(int, input().split())
A = list(map(int, input().split()))
A = [-a for a in A]
heapq.heapify(A)

for i in range(M):
    a = heapq.heappop(A)
    a /= 2
    heapq.heappush(A, a)

ans = 0
for a in A:
    ans += - a//1
print(int(ans))