N = int(input())
A = list(map(int,input().split()))

SerejaPoint = 0
DimaPoint = 0

for i in range(N):
    temp = max(A[0], A[-1])
    if i%2 == 0:
        SerejaPoint += temp
    else:
        DimaPoint += temp
    A.remove(temp)
print(SerejaPoint, DimaPoint)