K = int(input())
X,Y = map(int, input().split())

def main():
    if K%2 != (X+Y)%2:
        print(-1)
        return
    T = abs(X)+abs(Y)
    if T == K:
        print(1)
        print(X, Y)
        return
    if T < K:
        print(3)
        print(K,0)
        v = (K-T)//2
        print(X+K-v, Y-v)
        print(X,Y)
        return
    else:
        print(T//K+1)
        x,y = 0,0
        while abs(X-x)>K:
            x += (X-x)//abs(X-x)*K
            print(x,y)
        while abs(X-x)+abs(Y-y)>2*K:
            y += (Y-y)//abs(Y-y)*K
            print(x,y)
        if Y-y>0:
            t = [X-x, Y-K-y]
            v = (K-abs(t[0])-abs(t[1]))//2
            print(X+v, Y-K+v)
        else:
            t = [X-x, Y+K-y]
            v = (K-abs(t[0])-abs(t[1]))//2
            print(X+v, Y+K+v)
        print(X,Y)
        return

main()
