N, M = map(int, input().split())
A = list(map(int, input().split()))

costs = [2,5,5,4,5,6,3,7,6,1000]


def main():
    min_a = 10-1
    for a in A:
        if costs[a-1] < costs[min_a-1]:
            min_a = a
    rep = N//costs[min_a-1]
    res = N%costs[min_a-1]
    if res==0:
        print(str(min_a)*rep)
        return

    # two chars
    cands = []
    i = 1
    while costs[min_a-1]*i+res <= 7:
        for a in A:
            if (costs[min_a-1]*i+res) % costs[a-1] == 0:
                cands.append(a)
        if len(cands)>0:
            break
        i += 1
    if len(cands)>0:
        a = max(cands)
        rep = (N-costs[a-1]*i) // costs[min_a-1]
        if a>min_a:
            print(str(a)*i + str(min_a)*rep)
            return
        else:
            print(str(min_a)*rep + str(a)*i)
            return
    
    # three chars
    while costs[min_a-1]*i+res <= 14:
        for a0 in A:
            for a1 in A:
                if (costs[min_a-1]*i+res) % (costs[a0-1]+costs[a1-1]) == 0:
                    cands.append(a0*10+a1)
        if len(cands)>0:
            break
        i += 1
    if len(cands)>0:
        print(i)
        a = max(cands)
        a0 = a//10
        a1 = a%10
        rep = (N-i*(costs[a0-1]+costs[a1-1])) // costs[min_a-1]
        print(rep)
        if min_a < a1:
            print(str(a0)*i + str(a1)*i + str(min_a)*rep)
        elif min_a < a0:
            print(str(a0)*i + str(min_a)*rep + str(a1)*i)
        else:
            print(str(min_a)*rep + str(a0)*i + str(a1)*i)
        return

main()