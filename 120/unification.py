S = input()

red, blue = 0, 0
for s in S:
    if s=='0':
        red += 1
    else:
        blue += 1
ans = len(S) - abs(red-blue)
print(ans)