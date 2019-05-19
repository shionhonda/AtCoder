S = input()
s1 = int(S[:2])
s2 = int(S[2:])

if 1<=s1 and s1<=12 and 1<=s2 and s2<=12:
    print('AMBIGUOUS')
elif 1<=s1 and s1<=12 and (s2<1 or s2>12):
    print('MMYY')
elif 1<=s2 and s2<=12 and (s1<1 or s1>12):
    print('YYMM')
else:
    print('NA')