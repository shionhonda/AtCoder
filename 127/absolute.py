import bisect

Q = int(input())

A = []
B = 0

for _ in range(Q):
    q = input().split()
    if len(q)>1:
        __,a,b = map(int,q)
        i = bisect.bisect_left(A, a)
        A.insert(i, a)
        B += b
    else:
        i = (len(A)-1)//2
        a = A[i]
        s = B
        s += i*a - sum(A[:i])
        s += sum(A[i+1:]) - (len(A)-i-1)*a
        print(a, s)
