from collections import deque
test_case = 1

while True:
    P,C = map(int,input().split())
    if P == 0 and C == 0:
        break
    queue = deque()
    for i in range(1, min(P,C) + 1):
        queue.append(i)

    print('Case {}:'.format(test_case))
    test_case += 1

    for _ in range(C):
        line = input().split()
        command = line[0]
        if command == 'N':
            print(queue[0])
            queue.append(queue.popleft())
        else:
            x = int(line[1])
            n = len(queue)
            queue.append(x)
            for _ in range(n):
                temp = queue.popleft()
                if temp != x:
                    queue.append(temp)


