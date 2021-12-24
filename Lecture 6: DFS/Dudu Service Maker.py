
def DFS(source):
    flag[source] = True
    visited[source] = True
    for v in graph[source]:
        if flag[v]:
            answer = 'YES'
            return()
        if not visited[v]:
            DFS(v)
    flag[source] = False
    return()


Q = int(input())

for _ in range(Q):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    visited = [False]*(V+1)
    flag = [False]*(V+1)
    for _ in range(E):
        u,v = map(int,input().split())
        graph[u].append(v)
    answer = 'NO'
    for i in range(V):
        if not visited[i]:
            DFS(i)
    print(answer)
