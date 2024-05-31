def binary_search(arr, target, start, end):
    global ans
    if start > end:
        return -1
    mid = (start + end) // 2
    if arr[mid] == target:
        ans += 1
    binary_search(arr, target, mid + 1, end)
    binary_search(arr, target, start, mid - 1)

n, x = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0
binary_search(arr, x, 0, n - 1)
if ans:
    print(ans)
else:
    print(-1)