import queue
MAX = 505
INF = int(1e9)
graph = [[] for _ in range(MAX)]
dist = [INF for _ in range(MAX)]

class Node:
    def __init__(self,_id,_dist):
        self.dist = _dist
        self.id = _id

    def __lt__(self, other):
        return self.dist < other.dist

def Dijsktra(s):
    pq = queue.PriorityQueue()
    pq.put(Node(s,0))
    dist[s] = 0

    while not pq.empty():
        top = pq.get()
        u = top.id
        w = top.dist

        for neighbor in graph[u]:
            if w + neighbor.dist < dist[neighbor.id]:
                dist[neighbor.id] = w + neighbor.dist
                pq.put(Node(neighbor.id, dist[neighbor.id]))

n = int(input())

for _ in range(n):
    u,v,cost = map(int, input().split())
    graph[u].append(Node(v, cost))
    graph[v].append(Node(u,cost))
U = int(input())
Dijsktra(U)
Q = int(input())
for i in range(Q):
    v = int(input())
    if dist[v] != INF:
        print(dist[v])
    else:
        print("NO PATH")

