costs = [2,5,5,4,5,6,3,7,6]

N, M = map(int, input().split())
A = list(map(int, input().split()))
neginf = -1 * 1e20
D = [neginf]*(N+1)

def dp(n_match):
    D[0] = 0
    for n in range(1,n_match+1):
        arr = [D[n-costs[a-1]] if n-costs[a-1]>=0 else neginf for a in A]
        D[n] = max(arr)+1

def main():
    dp(N)
    n = N
    ans = ''
    while n>1:
        arr = [ a for a in A if  n-costs[a-1]>=0 and D[n-costs[a-1]]==D[n]-1 ]
        if len(arr)>0:
            a = max(arr)
            ans += str(a)
            n -= costs[a-1]
        else:
            break
    print(ans)

main()