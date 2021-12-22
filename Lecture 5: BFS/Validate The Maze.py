import queue
MAX = 21
visited = [[False] * MAX for _ in range(MAX)]
maze = [None]*MAX
dc = [1, -1, 0, 0]
dr = [0, 0, 1, -1]

class Cell:
    def __init__(self, _r, _c):
        self.r = _r
        self.c = _c

def isValid(r,c):
    return r in range(N) and c in range(M)

def isOnEdge(i,j):
    return i == 0 or j == 0 or i == N - 1 or j == M - 1

def BFS(s,f):
    q = queue.Queue()
    visited[s.r][s.c] = True
    q.put(s)

    while not q.empty():
        u = q.get()
        if u.r == f.r and u.c == f.c:
            return True
        for i in range(4):
            r = u.r + dr[i]
            c = u.c + dc[i]

            if isValid(r,c) and maze[r][c] == '.' and not visited[r][c]:
                visited[r][c] = True
                q.put(Cell(r,c))

    return False
Q = int(input())
for _ in range(Q):
    N,M = map(int,input().split())
    for i in range(N):
        maze[i] = input()

    entrance = []

    for i in range(N):
        for j in range(M):
            visited[i][j] = False
            if maze[i][j] == '.' and isOnEdge(i,j):
                entrance.append(Cell(i,j))
    if len(entrance) != 2:
        print('invalid')
    else:
        s = entrance[0]
        f = entrance[1]
        print('valid' if BFS(s,f) else 'invalid')



