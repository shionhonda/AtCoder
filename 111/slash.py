n = int(input())
V = input().split()

d0, d1 = {}, {}
for i in range(n//2):
    v = V[2*i]
    if v in d0:
        d0[v] += 1
    else:
        d0[v] = 1

    v = V[2*i+1]
    if v in d1:
        d1[v] += 1
    else:
        d1[v] = 1

s0 = sorted(d0.items(), key=lambda x: -x[1])
k0_0, v0_0 = s0[0]
s1 = sorted(d1.items(), key=lambda x: -x[1])
k1_0, v1_0 = s1[0]

if k0_0 != k1_0:
    print(n - v0_0 - v1_0)
else:
    k0_1, v0_1 = s0[1] if len(s0)>1 else ('0',0)
    k1_1, v1_1 = s1[1] if len(s1)>1 else ('0',0)
    if v0_0+v1_1 <= v0_1+v1_0:
        print(n - v1_0 - v0_1)
    else:
        print(n - v0_0 - v1_1)
