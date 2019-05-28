N = int(input())

SP = {}
for i in range(N):
    s, p = input().split()
    if s in SP.keys():
        SP[s].append([int(p), i])
    else:
        SP[s] = [[int(p), i]]
    
SP = sorted(SP.items(), key=lambda x:x[0], reverse=False)

for sp_set in SP:
    sps = sp_set[1]
    sps.sort(key=lambda x:x[0], reverse=True)
    for item in sps:
        print(item[1]+1)