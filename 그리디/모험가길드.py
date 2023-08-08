#1
n = int(input())
arr = list(map(int, input().split()))

group = 0

sets = set(arr)

for s in sets:
    group += arr.count(s) // s

print(group)