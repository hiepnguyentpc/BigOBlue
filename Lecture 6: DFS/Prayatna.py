def DFS(source):
    s = [source]
    visited[source] = True

    while len(s):
        u = s.pop()

        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                s.append(v)

T = int(input())

for _ in range(T):
    N = int(input())
    E = int(input())

    graph = [[] for _ in range(N)]
    visited = [False]*N

    for i in range(E):
        u,v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    count = 0

    for i in range(N):
        if visited[i] == False:
            DFS(i)
            count += 1

    print(count)