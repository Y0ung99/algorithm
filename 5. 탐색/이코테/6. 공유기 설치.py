import sys
n, c = map(int, input().split())
arr = []
for i in range(n):
    arr.append(int(sys.stdin.readline()))
arr.sort()
start = arr[1] - arr[0]
end = arr[-1] - arr[0]
result = 0

while start <= end:
    mid = (start + end) // 2
    value = arr[0]
    count = 1
    for i in range(1, n):
        if arr[i] >= value + mid:
            value = arr[i]
            count += 1
    if count >= c:
        start = mid + 1
        result = mid
    else:
        end = mid - 1
print(result)