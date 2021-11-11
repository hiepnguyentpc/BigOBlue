N = int(input())
T = [int(x) for x in input().split()]
curr = 0
for t in T:
    if t-curr <= 15:
        curr = t
    elif t-curr > 15:
        curr += 15
        break
    if t == T[len(T)-1]:
        if 90-t > 15:
            curr += 15
        elif 90-t < 15:
            curr += 90 - t
print(curr)