K, N, W = map(int, input().split())

W = W*(W+1)/2
result = K*W-N
if result < 0:
    result = 0
    print(result)
    exit()
else:
    print(int(result))
