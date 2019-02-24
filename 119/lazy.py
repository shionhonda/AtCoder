A, B, Q = map(int, input().split())
S = [int(input()) for _ in range(A)]
T = [int(input()) for _ in range(B)]
X = [int(input()) for _ in range(Q)]
INF = 10**12

def binary_search(query, arr):
    arr = [-INF] + arr + [INF]
    low = 0
    high = len(arr)
    t = (low+high)//2
    while low<high-1:
        if query>arr[t]:
            low = t
        else:
            high = t
        t = (low+high)//2
    return arr[low], arr[high]

def main():
    for x in X:
        s1, s2 = binary_search(x, S)
        t1, t2 = binary_search(x, T)
        ans = INF
        for s in [s1, s2]:
            for t in [t1, t2]:
                d1 = abs(t-x) + abs(s-t)
                d2 = abs(s-x) + abs(t-s)
                ans = min(ans, d1, d2)
        print(ans)
    return

main()