N, M = map(int, input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

i = j = 0
while i < N and j < M:
    if A[i] <= B[j]:
        i += 1
    j += 1

print(N-i)
