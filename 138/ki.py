class Node:
    def __init__(self, id, parent=None):
        self.id = id
        self.parent = parent
        self.children = []

    def add(self, n):
        counter[self.id] += n
        for child in self.children:
            child.add(n)

N, Q = map(int, input().split())
tree = [None] * N
counter = [0] * N
tree[0] = Node(0) # root (1)
for i in range(N-1):
    a, b = map(int, input().split())
    tree[b-1] = Node(b-1, a-1)
    tree[a-1].children.append(tree[b-1])

for i in range(Q):
    p, x = map(int, input().split())
    tree[p-1].add(x)
    
print(' '.join(list(map(str, counter))))