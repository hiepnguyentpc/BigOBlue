N = int(input())
A = list(map(int,input().split()))

i = 1
while i < N and A[i] > A[i-1]:
    i += 1

j = i
while j < N and A[j] < A[j-1]:
    j += 1

temp = []
for var in range(0, i-1):
    temp.append(A[var])
for var in range(i, j-1):
    temp.append(A[var])
for var in range(j, N-1):
    temp.append(A[var])

print(temp)
A.sort()
print(A)
#if temp == A:
#    print("yes")
#    print(i,j)
#else:
#    print("no")