N, M = map(int, input().split())
A = [int(input()) for _ in range(M)]
DIV = 10**9+7

def main():
    if M>0:
        B = [0]*(M+1)
        for i in range(M+1):
            if i==0:
                B[i] = A[i]-1
            elif i==M:
                B[i] = N-A[i-1]-1
            else:
                if A[i]==A[i-1]:
                    B[i] = 0
                else:
                    B[i] = A[i] - A[i-1] - 2
    else:
        B = [N]
    min_B = min(B)
    if min_B<0:
        return 0
    
    max_B = max(B)
    F = [1]*(max_B+1)
    for i in range(max_B+1):
        if i<2:
            pass
        else:
            F[i] = F[i-2] + F[i-1]
    ans = 1
    for b in B:
        ans *= F[b]
        if ans >= DIV:
            ans %= DIV
    return ans

print(main())
