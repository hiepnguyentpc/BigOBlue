import queue
MAX = 100
INF = int(1e9)
class Node:
    def __init__(self,id,dist):
        self.dist = dist
        self.id = id
    def __lt__(self, other):
        return self.dist <= other.dist

def Dijsktra(s):
    pq = queue.PriorityQueue()
    pq.put(Node(s,0))
    dist[s] = 0
    while pq.empty() == False:
        top = pq.get()
        u = top.id
        w = top.dist
        for neighbor in graph[u]:
            if w + neighbor.dist < dist[neighbor.id]:
                dist[neighbor.id] = w + neighbor.dist
                pq.put(Node(neighbor.id, dist=[neighbor.id]))
                path[neighbor.id] = u

if __name__ == '__main__':
    n = int(input())
    graph = [[] for i in range(n+5)]
    dist = [INF for i in range(n+5)]
    path = [-1 for i in range(n+5)]
    for i in range(n):
        u,v,cost = list(map(int, input().split()))
        graph[u].append(Node(v, cost))
        graph[v].append(Node(u,cost))
    U = int(input())
    Dijsktra(U)
    Q = int(input())
    for i in range(1,Q-1):
        v = int(input())
        if dist[v] != INF:
            print(dist[v])
        else:
            print("No path")

