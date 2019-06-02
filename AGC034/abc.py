S = input()
S = S.replace('BC', 'X')

ans = 0
acc_A = 0
for s in S:
    if s=='A':
        acc_A += 1
    elif s=='X':
        ans += acc_A
    else:
        acc_A = 0

print(ans)