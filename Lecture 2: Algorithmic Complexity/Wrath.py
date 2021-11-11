N = int(input())
A = list(map(int,input().split()))

kills = 0
j = N - 1

for i in range(len(A) - 1, -1, -1):
    if j > i: j = i
    last_kill = max(0,i - A[i]) #loai truong hop mong vuot cham den cuoi array
    if last_kill < j:
        kills += j - last_kill
        j = last_kill
print(N - kills)
