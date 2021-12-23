MAX = 1001
graph = [[] for _ in range(MAX)]
visited = [False]*MAX
dist = [0]*MAX


N = int(input())
for i in range(N-1):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

def DFS(source):
    s = []
    s.append(source)
    visited[source] = True
    while len(s) > 0:
        u = s.pop()
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                s.append(v)
                dist[v] = dist[u]+1
DFS(1)

ans = 0
min_dist = MAX
Q = int(input())
for _ in range(Q):
    u = int(input())
    if dist[u] < min_dist or (dist[u] == min_dist and u < ans):
        min_dist = dist[u]
        ans = u

print(ans)