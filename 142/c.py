import numpy as np

N = int(input())
A = list(map(int, input().split()))
A = np.array(A)

B = np.argsort(A) + 1
B = list(map(str, B))
print(' '.join(B))
