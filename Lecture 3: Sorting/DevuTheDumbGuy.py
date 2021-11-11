N, X = map(int, input().split())
C = list(map(int,input().split()))
C.sort()

result = 0
for i in range(len(C)):
    result += X*C[i]
    if X > 1:
        X -= 1

print(result)