N = int(input())
A = list(map(int,input().split()))

result = []
for i in range(0, N):
    sum = 1
    for j in range(0,N):
        if A[i] < A[j]:
            sum += 1
    result.append(sum)

print(*result)