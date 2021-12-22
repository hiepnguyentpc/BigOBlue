import queue
MAX = 100001
MOD = 100000

s, f = map(int, input().split())
N = int(input())
A = list(map(int, input().split()))

def BFS(s,f):
    q = queue.Queue()
    dist = [-1]*MAX
    q.put(s)
    dist[s] = 0

    while not q.empty():
        u = q.get()

        for x in A:
            v = (u*x)%MOD
            if dist[v] == -1:
                dist[v] = dist[u]+1
                q.put(v)
            if v == f:
                return dist[v]
    return -1

print(BFS(s,f))