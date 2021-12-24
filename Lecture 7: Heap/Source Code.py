
def minHeapify(i):
    smallest = i
    left = 2*i + 1
    right = 2*i + 2
    #nếu child node trái nhỏ hơn root
    if left < len(h) and h[left] < h[smallest]:
        smallest = left
    #nếu child node phải nhỏ hơn root
    if right < len(h) and h[right] < h[smallest]:
        smallest = right
    #swap hai node nếu có thể, sắp xếp lại toàn bộ cây con
    if smallest != i:
        h[i], h[smallest] = h[smallest], h[i]
        minHeapify(smallest)


def buildHeap(n):
    for i in range(n//2 - 1, -1 , -1): #// là floor division
        minHeapify(i)

if __name__ == '__main__':
    h = [7,12,6,10,17,15,2,4]
    buildHeap(len(h))
    print(h)