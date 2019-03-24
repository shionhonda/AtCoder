N = int(input())
black1 = ["AGC", "GAC", "ACG"]
black2 = ["AAGC", "ACGC", "AGGC", "ATGC",
        "AGAC", "AGCC", "AGGC", "AGTC"]
memo = [{} for _ in range(N+1)]

def func(cur, S):
    if S[-3:] in black1:
        return 0
    if S[-4:] in black2:
        return 0
    if S[-3:] in memo[cur]:
        return memo[cur][S[-3:]]
    else:
        if cur==N:
            return 1
        ret = 0
        for s in "ACGT":
            ret = ret + func(cur+1, S+s)
        memo[cur][S[-3:]] = ret
        return ret


print(func(0, "____")%(10**9+7))