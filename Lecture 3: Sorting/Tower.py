N = int(input())
L = list(map(int,input().split()))

elements_count = {}
count = 0
for element in L:
   if element in elements_count:
      elements_count[element] += 1
   else:
      elements_count[element] = 1

temp = 0
for element in L:
    temp = max(temp, elements_count[element])

print(temp ,len(elements_count.keys()))
