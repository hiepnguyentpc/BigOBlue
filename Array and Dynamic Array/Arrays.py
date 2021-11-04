temp = input()
K, M = map(int, input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))


if A[K-1] < B[-M]:
    print("YES")
else:
    print("NO")

