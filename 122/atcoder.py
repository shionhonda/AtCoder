S = input()
acgt = ["A", "T", "G", "C"]

def main(S):
    cnt = 0
    m = 0
    for s in S:
        if s not in acgt:
            cnt = 0
        else:
            cnt += 1
        m = max(m, cnt)
    return m

print(main(S))