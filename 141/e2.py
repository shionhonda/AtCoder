N = int(input())
S = input()

def search(w):
    dic = {}
    for i in range(N+1-w):
        s = S[i:i+w]
        if s not in dic.keys():
            dic[s] = [i]
        else:
            if dic[s][0]+w<=i:
                return True
            dic[s].append(i)
    return False

def main():
    ans = 0
    max_w = N//2
    for i in range(1, max_w+1):
        if search(i):
            ans = i
        else:
            break
    print(ans)

main()
