Q = int(input())
MAX = 10**6+3

def multiple(x, d, n):
    ans = x
    X = x
    for _ in range(n-1):
        X += d
        ans *= X
        ans = ans % MAX
        if ans == 0:
            break
    return ans

for _ in range(Q):
    x,d,n = map(int, input().split())
    print(multiple(x,d,n))