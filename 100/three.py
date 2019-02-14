N = int(input())
A = map(int, input().split())

s = 0
for a in A:
    while a%2==0:
        s += 1
        a = a//2
print(s)