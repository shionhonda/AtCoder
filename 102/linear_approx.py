N = int(input())
A = list(map(int, input().split()))
B = A.copy()
for i in range(N):
    B[i] -= i+1
B.sort()
if N%2==0:
    n = N//2
    b = (B[n-1]+B[n]) // 2
else:
    b = B[(N-1)//2]
ans = 0
for i,a in enumerate(A):
    ans += abs(a - (b+i+1))
print(ans)
