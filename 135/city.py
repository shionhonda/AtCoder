N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
B.append(0)

cnt = 0
carry = 0
for i in range(N+1):
    #print(carry, B[i], A[i])
    cnt += min(A[i], carry+B[i])
    carry = max(0, B[i]-max(0,A[i]-carry))
    #print(cnt, '\n')

print(cnt)