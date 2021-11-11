N = int(input())
A = list(map(int,input().split()))

right = 0
best = 0
count = 0
freq = [0] * 100001

for left in range(0, N - 1):
    while count <= 2 and right < N:
        if count == 2 and freq[A[right]] == 0:
            break
        if freq[A[right]] == 0:
            count += 1
        freq[A[right]] += 1
        right += 1
    best = max(right - left, best)
    if freq[A[left]] == 1:
        count -= 1
    freq[A[left]] -= 1

print(best)