N = int(input())
a = 10**9
b = 0
coordinate_List = []
for _ in range(N):
    x,y = map(int, input().split())
    a = min(a,x)
    b = max(b,y)
    coordinate_List.append((x,y))

if(a,b) in coordinate_List:
    print(coordinate_List.index((a,b)) + 1)
else:
    print("-1")
