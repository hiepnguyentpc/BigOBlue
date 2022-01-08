import heapq
top3 = [] #maxheap
rest = [] #minheap
#to implement a maxheap, put a - mark in front of element
number_Review = 0

n = int(input())

for _ in range(n):
    line = list(map(int, input().split()))
    if line[0] == 1:
        x = line[1]
        number_Review += 1

        if len(top3) != 0 and x > top3[0]:
                #push the top element of top3 to the rest
                heapq.heappush(rest, -heapq.heappop(top3))
                #push element x to top3 (max_heap)
                heapq.heappush(top3, x)
        else:
            heapq.heappush(rest,-x)
        if number_Review % 3 == 0:
            heapq.heappush(top3, -heapq.heappop(rest))
    else:
        if len(top3) == 0:
            print("No reviews yet")
        else:
            print(top3[0])



