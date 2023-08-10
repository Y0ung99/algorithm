from itertools import combinations

n, m = map(int, input().split())
arr = list(map(int, input().split()))

arr = list(combinations(arr, 2))
remove_set = set()

for e in arr:
    if e[0] == e[1]:
        remove_set.add(e)

result = [i for i in arr if i not in remove_set]

print(len(result))
