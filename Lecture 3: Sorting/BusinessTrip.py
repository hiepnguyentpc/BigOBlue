K = int(input())
A = list(map(int,input().split()))
sum=0
i=0
A.sort(reverse=True)
while(sum < K and i<12):
    sum += A[i]
    i += 1
if(sum >= K):
    print(i)
else:
    print(-1)