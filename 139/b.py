import math
A, B = map(int, input().split())

c = (B-A)/(A-1) + 1
print(math.ceil(c))