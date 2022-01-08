INF = 10**9

class Edge:
    def __init__(self, _source, _destination, _weight):
        self.source = _source
        self.destination = _destination
        self.weight = _weight

def BellmanFord(s):
    dist[s] = 0
    for i in range(N-1):
        for j in range(M):
            u = graph[j].source
            v = graph[j].destination
            w = graph[j].weight
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    for j in range(N):
        for i in range(M):
            u = graph[i].source
            v = graph[i].destination
            w = graph[i].weight
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = -INF

T = int(input())

for t in range(1,T+1):
    input()
    N = int(input())
    busyness = [0] + list(map(int, input().split()))

    dist = [INF] * (N+1)
    graph = []

    M = int(input())
    for _ in range(M):
        u,v = map(int,input().split())
        w = (busyness[v] - busyness[u])**3
        graph.append(Edge(u,v,w))

    BellmanFord(1)
    Q = int(input())
    print("Case {}:".format(t))

    for _ in range(Q):
        dest = int(input())
        print(dist[dest] if dist[dest] != INF and dist[dest] >= 3 else "?")