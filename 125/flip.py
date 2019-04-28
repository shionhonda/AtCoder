N = int(input())
A = list(map(int, input().split()))

ans = 0
pc, zc, mc = 0, 0, 0
s = 0
min_abs = 10**9
for a in A:
    abs_a = abs(a)
    min_abs = min(min_abs, abs_a)
    s += abs_a
    if a>0:
        pc += 1
    elif a==0:
        zc += 1
    else:
        mc += 1

if zc>0 or mc%2==0:
    print(s)
else:
    print(s-2*min_abs)
