a, b = map(int, input().split())
A = min(a,b)
B = max(a,b)

def main():
    if A==B:
        print(K)
        return
    elif (A+B)%2 == 0:
        print((A+B)//2)
        return
    else:
        print('IMPOSSIBLE')
        return

main()