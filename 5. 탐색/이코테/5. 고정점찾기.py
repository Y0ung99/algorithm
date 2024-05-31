def binary_search(arr, start, end):
    if start > end:
        return -1
    mid = (start + end) // 2
    if arr[mid] == mid:
        return mid
    elif arr[mid] < mid:
        return binary_search(arr, mid+1, end)
    elif arr[mid] > mid:
        return binary_search(arr, start, mid-1)

n = int(input())
arr = list(map(int, input().split()))
print(binary_search(arr, 0, n-1))