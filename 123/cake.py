X, Y, Z, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A.sort(reverse=True)
B.sort(reverse=True)
C.sort(reverse=True)

ans_list = []
for x,a in enumerate(A):
    for y,b in enumerate(B):
        if (x+1)*(y+1)>K:
                break
        for z,c in enumerate(C):
            if (x+1)*(y+1)*(z+1)>K:
                break
            ans_list.append(a+b+c)

ans_list.sort(reverse=True)

for ans in ans_list[:K]:
    print(ans)