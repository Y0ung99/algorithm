for test_case in range(11):
    n = int(input())
    arr = list(map(int, input().split()))
    for i in range(n):
        h_idx = arr.index(max(arr))
        l_idx = arr.index(min(arr))
        if arr[h_idx] - arr[l_idx] <= 1:
            break
        arr[h_idx] -= 1
        arr[l_idx] += 1
    print(f"#{test_case+1} {max(arr) - min(arr)}")