N = int(input())
A = list(map(int, input().split()))

x = 0
for i,a in enumerate(A):
    if i%2==0:
        x += a
    else:
        x -= a
ans = [str(x)]
for i in range(1,N):
    x = 2*A[i-1] - x
    ans.append(str(x))

print(' '.join(ans))