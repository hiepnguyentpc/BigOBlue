N = int(input())
list = [int(x) for x in input().split()]
count = 0

if N == 1:
    if list[0] == 1:
        print("YES")
        exit()
    else:
        print("NO")
        exit()

for A in list:
    if (A == 0):
        count += 1
if count > 1:
    print("NO")
    exit()
elif count == 1:
    print("YES")
    exit()
else:
    print("NO")
    exit()