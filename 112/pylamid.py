N = int(input())
S = [ list(map(int, input().split())) for _ in range(N) ]

def main():
    for i in range(101):
        for j in range(101):
            H = 0
            for x,y,h in S:
                if h==0:
                    continue
                else:
                    H = h+abs(x-i)+abs(y-j)
                    break
            flg = True
            for x,y,h in S:
                if h != max(0, H-abs(x-i)-abs(y-j)):
                    flg = False
                    break
            if flg:
                print(i, j, H)
                return

main()
