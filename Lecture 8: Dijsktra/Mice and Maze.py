MAX = 101
INF = int(1e9) + 1
dist = [INF for _ in range(MAX)]
graph = [[] for _ in range(MAX)]
import queue
class Node:
    def __init__(self, _id, _dist):
        self.dist = _dist
        self.id = _id
    def __lt__(self, other):
        return self.dist <= other.dist

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

N = int(input())
E = int(input())
T = int(input())
M = int(input())

for _ in range(M):
    line = list(map(int,input().split()))
    U = line[0]
    V = line[1]
    W = line[2]
    graph[V].append(Node(U,W))

Dijsktra(E)

count = 0
for i in range(1,N+1):
    if dist[i] <= T:
        count += 1

print(count)