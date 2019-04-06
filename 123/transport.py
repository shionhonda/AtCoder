import math

N = int(input())
m = 1<<50
for _ in range(5):
    tmp = int(input())
    m = min(m, tmp)

print(math.ceil(N/m)+4)