a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
X = [a,b,c,d,e]
t = 0

m = 10
for x in X:
    if x%10==0:
        t += x
    else:
        t += (x//10+1) * 10
        m = min(m, x%10)
t = t - 10 + m
print(t)