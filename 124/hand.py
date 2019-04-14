N, K = map(int, input().split())
S = input()

arr = []
cnt = 0
comp = S[0]
for s in S:
    if s==comp:
        cnt += 1
    else:
        arr.append(cnt)
        cnt = 1
        comp = s
arr.append(cnt)

if len(arr)<3:
    print(sum(arr))
else:
    if S[0]=='1':
        L = (len(arr)+1)//2 - K +1
        l = 0
        tmp = sum(arr[2*l:2*(l+K)+1])
        ans = tmp
        for l in range(1, L):
            tmp = tmp - (arr[2*(l-1)]+arr[2*l-1]) + sum(arr[2*(l-1+K)+1 : min(2*(l+K)+1, len(arr))])
            ans = max(tmp, ans)
    else:
        L = (len(arr)+1)//2 - K + 1
        l = 0
        tmp = sum(arr[2*l:2*(l+K)])
        ans = tmp
        for l in range(1, L):
            tmp = tmp - sum(arr[max(0,2*l-3) : 2*l-1]) + sum(arr[2*(l+K-1): min(2*(l+K), len(arr))])
            ans = max(tmp, ans)
            
    print(ans)