N, Q = map(int, input().split())

cond = {}
for _ in range(N):
    s, t, x = map(int, input().split())
    if x not in cond.keys():
        cond[x] = [[s-x, t-x]]
    else:
        cond[x].append([s-x, t-x])
cond = sorted(cond.items(), key=lambda x:x[0], reverse=False)

def walk(d):
    for x,cs in cond:
        flg = True
        for c in cs:
            s, t = c
            if d < s or t <= d:
                pass
            else:
                flg = False
                break
        if not flg:
            return x
    return -1


D = [int(input()) for _ in range(Q)]
for d in D:
    print(walk(d))
    