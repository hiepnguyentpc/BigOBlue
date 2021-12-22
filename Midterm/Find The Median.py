import statistics

N = int(input())
items = list(map(int, input().split()))

print(statistics.median(items))