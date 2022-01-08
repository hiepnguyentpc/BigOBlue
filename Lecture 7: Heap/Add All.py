import queue

q = queue.PriorityQueue()
while True:
    N = int(input())
    if N == 0:
        break


    for item in input().split():
        q.put(int(item))

    result = 0
    while q.qsize() > 1:
        a = q.get()
        b = q.get()
        result += a+b
        q.put(a+b)
    print(result)
    q.get()