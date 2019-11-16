import itertools

N = int(input())
X = [list(map(int, input().split())) for _ in range(N)]

def dist(perm):
    d = 0
    x0, y0 = X[perm[0]]
    for i in perm[1:]:
        x1, y1 = X[i]
        d += ((x1-x0)**2 + (y1-y0)**2)**0.5
        x0 = x1
        y0 = y1
    return d

def main():
    d = 0
    perms = list(itertools.permutations(range(N)))
    for perm in perms:
        d += dist(perm)
    return d/len(perms)

print(main())