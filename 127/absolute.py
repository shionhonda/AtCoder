import bisect

Q = int(input())

A = []
B = 0
S1, S2 = [], []
for _ in range(Q):
    q = input().split()
    if len(q)>1:
        __,a,b = map(int,q)
        i = bisect.bisect_left(A, a)
        A.insert(i, a)
        if i>0:
            S1.insert(i, S1[i-1])
        else:
            S1.insert(i, 0)
        for k in range(i,len(S1)):
            S1[k] += a
        j = len(S2)-i
        if j>0:
            S2.insert(j, S2[j-1])
        else:
            S2.insert(j, 0)
        for k in range(j,len(S2)):
            S2[k] += a 
        B += b
    else:
        i = (len(A)-1)//2
        a = A[i]
        s = S2[i]-S1[i]+B
        print(a, s)
