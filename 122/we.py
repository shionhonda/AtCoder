N = int(input())
black_list= [
    "GACA", "GACC", "GACG", "GACT",
    "ACGA", "ACGC", "ACGG", "ACGT",
    "AGAC", "AGCC", "AGGC", "AGTC",
    "AGCA", "AGCG", "AGCT",
    "AAGC", "ATGC",
    "CAGC", "GAGC", "TAGC",
    "CGAC", "GGAC", "TGAC",
    "AACG", "CACG", "TACG"
]

def func(S):
    if N==3:
        return 61
    if S[-4:] in black_list:
        return 0
    else:
        if len(S)-4==N:
            return 1
        return func(S+"A") + func(S+"C") + func(S+"G") + func(S+"T")


print(func("____"))