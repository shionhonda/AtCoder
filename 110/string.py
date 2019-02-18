S = input()
T = input()

def judge(s1, s2):
    d = {}
    for i,c in enumerate(s1):
        if c not in d:
            d[c] = [i]
        else:
            d[c].append(i)
    for v in d.values():
        a = v[0]
        for b in v:
            if s2[a]!=s2[b]:
                return 0
            a = b
    return 1

if judge(S,T)*judge(T,S) == 1:
    print('Yes')
else:
    print('No')