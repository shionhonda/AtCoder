N = int(input())
A = list(map(int, input().split()))

def euclid(a, b):
    m = min(a,b)
    n = max(a,b)
    if (n%m==0):
        return m
    else:
        return euclid(m, n%m)

def lcm(X):
    a = X[0]
    for x in X[1:]:
        a = a* x // euclid(a,x)
    return a

y = lcm(A)-1
s = 0
for a in A:
    s += y%a
print(s)
