N, A, B = map(int, input().split())
H = list(map(int,input().split()))

H.sort()
print(H[B] - H[B-1])
