N = int(input())
A = list(map(int, input().split()))

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

L, R = [0]*(N+1), [0]*(N+1)
for i in range(1,N+1):
    L[i] = gcd(L[i-1], A[i-1])
    R[N-i] = gcd(R[N+1-i], A[N-i])

ans = 0
for i in range(N):
    ans = max(ans, gcd(L[i], R[i+1]))

print(ans)