S = input()

ans = 'Yes'
for i, s in enumerate(S):
    if (i+1)%2==1:
        if s=='L':
            ans = 'No'
    else:
        if s=='R':
            ans = 'No'

print(ans)