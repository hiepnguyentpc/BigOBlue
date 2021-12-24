import queue
q = queue.PriorityQueue()
qRemove = queue.PriorityQueue()
Q = int(input())

for _ in range(Q):
    line = list(map(int,input().split()))
    if  line[0] == 1:
        q.put(line[1])
    elif line[0] == 2:
        qRemove.put(line[1])
    elif line[0] == 3:
        while not qRemove.empty() and q.queue[0] == qRemove.queue[0]:
            qRemove.get()
            q.get()
        print(q.queue[0])
