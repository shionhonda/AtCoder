N = int(input())
cands = '753'

def dfs(s):
    if int(s)>N:
        return 0
    if '7' in s and '5' in s and '3' in s:
        ret = 1
    else:
        ret = 0
    for c in cands:
        ret += dfs(s+c)
    return ret

print(dfs('0'))
