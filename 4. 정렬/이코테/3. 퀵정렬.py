def q_sort(arr, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        while left <= end and arr[left] <= arr[pivot]: # 9 <= 5
            left += 1
        while right > start and arr[right] >= arr[pivot]:
            right -= 1
        if left > right:
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else:
            arr[left], arr[right] = arr[right], arr[left]
    q_sort(arr, start, right-1)
    q_sort(arr, right+1, end)

def py_q_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    tail = arr[1:]

    left = [x for x in tail if x <= pivot]
    right = [x for x in tail if x > pivot]
    return py_q_sort(left) + [pivot] + py_q_sort(right)

arr = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
arr = py_q_sort(arr)
print(arr)