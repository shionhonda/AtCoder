N = int(input())
S = list(map(int, input().split()))

dic = {}
for s in S:
    if s not in dic:
        dic[s] = 1
    else:
        dic[s] += 1
tups = sorted(dic.items(), key=lambda x:x[0], reverse=True)

def main():
    orig, num = tups[0]
    for tup in tups[1:]:
        if tup[1] > num*N:
            print('No')
            return
        orig, num = tup
    print('Yes')

main()