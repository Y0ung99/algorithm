n = int(input())
arr = list(map(int, input().split()))
arr.sort()
target = 1

for a in arr:
    if a <= target:
        target += a
    else:
        break
print(target)