INF = 10**9

class Edge:
    def __init__(self, _source, _target, _weight):
        self.source = _source
        self.target = _target
        self.weight = _weight

def BellmanFord(s):
    dist = [INF for _ in range(N)]
    dist[s] = 0
    for i in range(N-1):
        for j in range(len(graph)):
            u = graph[j].source
            v = graph[j].target
            w = graph[j].weight
            if dist[u] != INF and (dist[u] + w < dist[v]):
                dist[v] = dist[u] + w

    for i in range(len(graph)):
        u = graph[i].source
        v = graph[i].target
        w = graph[i].weight
        if dist[u] != INF and (dist[u] + w < dist[v]):
            return False

    return True

T = int(input())

for _ in range(T):
    N,M = map(int, input().split())
    graph = []
    for i in range(M):
        source, target, weight = map(int, input().split())
        graph.append(Edge(source, target, weight))

    print("possible" if not BellmanFord(0) else "not possible")