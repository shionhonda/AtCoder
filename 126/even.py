N = int(input())
arr = [None]*N
visited = [False]*N
UVW = []

class Node:
    def __init__(self, id):
        self.id = id
        self.friends = []
        self.color = None

    def add_friend(self, friend, w):
        self.friends.append([friend.id, w)
        friend.friends.append([self.id, w])
        
nodes = [Node(i) for i in range(1,N+1)]
for i in range(N-1):
    u, v, w = map(int, input().split())
    nodes[u-1].add_friend(nodes[v-1])
    
def color_friend(node):
    for friend,w in node.friends:
        if friend.color is not None:
            continue
        


while True:



for i,uvw in enumerate(UVW):
    u,v,w = uvw
    if i==0:
        arr[u-1] = 0
        visited[u-1] = True
    if visited[u-1]:
        arr[v-1] = arr[u-1] + w
        visited[v-1] = True
    elif visited[v-1]:
        arr[u-1] = arr[v-1] + w
        visited[u-1] = True
    
print(arr)
for a in arr:
    if a%2==0:
        print(0)
    else:
        print(1)