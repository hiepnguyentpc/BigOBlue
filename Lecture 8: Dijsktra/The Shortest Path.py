import queue


class Node:
    def __init__(self, _id, _dist):
        self.dist = _dist
        self.id = _id
    def __lt__(self, other):
        return self.dist <= other.dist

def Dijsktra(s,f):
    pq = queue.PriorityQueue()
    pq.put(Node(s,0))
    dist = [10**9 for _ in range(N+1)]
    dist[s] = 0


    while not pq.empty():
        top = pq.get()
        u = top.id
        w = top.dist

        if u == f:
            break

        for neighbor in graph[u]:
            if w + neighbor.dist < dist[neighbor.id]:
                dist[neighbor.id] = w + neighbor.dist
                pq.put(Node(neighbor.id, dist[neighbor.id]))

    return dist[f]

S = int(input())

for _ in range(S):
    N = int(input())
    graph = [[] for _ in range(N+1)]
    city_name = []

    for city in range(1, N+1):
        name = input()
        city_name.append(name)
        neighbor_number = int(input())

        for _ in range(neighbor_number):
            v, w = map(int, input().split())
            graph[city].append(Node(v,w))

    R = int(input())

    for _ in range(R):
        source_city, finish_city = input().split()
        s = city_name.index(source_city)+1
        f = city_name.index(finish_city)+1
        print(Dijsktra(s,f))

    input()