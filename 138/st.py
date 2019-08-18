import bisect

S = list(input())
T = list(input())

s_dic = {}
for i,s in enumerate(S):
    if s not in s_dic.keys():
        s_dic[s] = [i]
    else:
        s_dic[s].append(i)

def main():
    pre, n_repeat = -1, 0
    cur = -1
    for t in T:
        if t not in s_dic.keys():
            return -1
        i = bisect.bisect_right(s_dic[t], cur)
        if i >= len(s_dic[t]):
            cur = s_dic[t][0]
            n_repeat += 1
        else:
            cur = s_dic[t][i]
            if cur <= pre:
                n_repeat += 1
        pre = cur
            
    return n_repeat * len(S) + cur + 1

print(main())