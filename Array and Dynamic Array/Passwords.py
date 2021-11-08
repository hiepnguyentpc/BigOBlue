import math

n, k = map(int, input().split())

passwords = []
for _ in range(n):
    passwords.append(input())
passwordKey = input()
count1 = 0
count2 = 0
for password in passwords:
    if len(password) < len(passwordKey):
        count1 += 1
    if len(password) <= len(passwordKey):
        count2 += 1

best_case = count1 + math.floor((count1/k))*5 + 1
worst_case = count2 + math.floor((count2 - 1)/k)*5
print(int(best_case),int(worst_case))