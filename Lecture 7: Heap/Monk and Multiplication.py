
N = int(input())
A = list(map(int, input().split()))

def maxHeapify(i):
    largest = i
    left = i*2 + 1
    right = i*2 + 2

    if left < len(A_heap) and A_heap[left] > A_heap[largest]:
        largest = left
    if right < len(A_heap) and A_heap[right] > A_heap[largest]:
        largest = right
    if largest != i:
        A_heap[largest], A_heap[i] = A_heap[i], A_heap[largest]
        maxHeapify(largest)

def buildHeap(n):
    for i in range(n//2 - 1, -1, -1):
        maxHeapify(i)


A_heap = []
for i in range(len(A)):
    A_heap.append(A[i])
    if i < 2:
        print(-1)
    else:
        buildHeap(len(A_heap))
        print(A_heap)
        print(A_heap[0]*A_heap[1]*A_heap[2])


"""
import queue

n = int(input())
a = list(map(int, input().split()))
pq = queue.PriorityQueue()

for i in range(n):
    pq.put(-a[i])

    if i < 2:
        print(-1)

    else:
        first = -pq.get()
        second = -pq.get()
        third = -pq.get()
        print(pq.queue)
        print(first*second*third)

        pq.put(-first)
        pq.put(-second)
        pq.put(-third)
"""