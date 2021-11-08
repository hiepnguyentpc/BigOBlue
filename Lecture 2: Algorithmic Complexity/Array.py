N, K = map(int, input().split())
A = list(map(int,input().split()))
count = 0
elements_count = {}
L = 0
R = N-1
for element in A:
    if element in elements_count:
        elements_count[element] += 1
    else:
        elements_count[element] = 1
for element in elements_count:
    if elements_count[element] != 0:
        count += 1
if count < K:
    print("-1 -1")
else:
    while(count >= K):
        elements_count[A[R]] -= 1
        if elements_count[A[R]] == 0:
            count -= 1
        R -= 1
    R += 1
    elements_count[A[R]] += 1
    count += 1

    while(count >= K):
        elements_count[A[L]] -= 1
        if elements_count[A[L]] == 0:
            count -= 1
        L += 1
    L -= 1
    elements_count[A[L]] += 1
    count += 1

    print(L+1, R+1)