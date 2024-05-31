def binary_search(arr, target, start, end):
    print(start, end)
    if start > end:
        return None
    mid = (start + end) // 2
    temp = sum(list(map(lambda x: x-mid if x-mid > 0 else 0, arr)))
    if temp == target:
        return mid
    elif temp < target:
        return binary_search(arr, target, start, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, end)

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
print(binary_search(arr, m, 0, arr[n-1]))