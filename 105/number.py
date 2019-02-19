N = int(input())
A = [[0,1] for _ in range(31)]
a = 1
for i in range(1,31):
    a *= -2
    A[i][0] = A[i-1][0] + min(0,a)
    A[i][1] = A[i-1][1] + max(0,a)
a = 1
for i in range(0,31):
    a *= -2
    A[i][0] += a
    A[i][1] += a
A = [[1,1]] + A
A = A[:32]

def main():
    if N==0:
        return '0'
    s = ''
    n = N
    flg = False
    for i in range(31, -1, -1):
        if A[i][0]<=n and n<=A[i][1]:
            s += '1'
            n -= (-2)**i
            flg = True
        else:
            if flg:
                s += '0'
    return s

print(main())
