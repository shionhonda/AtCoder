N, k = map(int, input().split())
S = input()
t = ''
for i in range(N):
    if i!=k-1:
        t += S[i]
    else:
        t += S[i].lower()
print(t)

