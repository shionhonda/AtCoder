A, B, Q = map(int, input().split())
INF = 10**12
S = [-INF] + [int(input()) for _ in range(A)] + [INF]
T = [-INF] + [int(input()) for _ in range(B)] + [INF]
X = [int(input()) for _ in range(Q)]


def binary_search(query, arr):
    low = 0
    high = len(arr)
    while high-low>1:
        mid = (low+high)//2
        if query>arr[mid]:
            low = mid
        else:
            high = mid
    return arr[low], arr[high]

def main():
    for x in X:
        s1, s2 = binary_search(x, S)
        t1, t2 = binary_search(x, T)
        ans = [ abs(t-s)+min(abs(t-x), abs(s-x)) \
            for t in [t1, t2] for s in [s1, s2] ]
        print(min(ans))
    return

main()