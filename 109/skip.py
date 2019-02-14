n,o = map(int, input().split())
X = list(map(int, input().split()))
X = [abs(x-o) for x in X]

def euclid(a, b):
    if a>b:
        tmp = a
        a = b
        b = tmp
    while a>0:
        c = b%a
        b = a
        a = c
    return b

def sub_gcd(X):
    Y = []
    P, Q = len(X)//2, len(X)%2
    for p in range(P):
        y = euclid(X[2*p], X[2*p+1])
        Y.append(y)
    if Q!=0:
        Y.append(X[-1])
    return Y

def gcd(X):
    Y = sub_gcd(X)
    while len(Y)>1:
        Y = sub_gcd(Y)
    return Y[0]

print(gcd(X))
