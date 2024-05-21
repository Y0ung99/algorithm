T = int(input())

def dfs(i, result):
    global count
    if result == k:
        count += 1
        return
    if i == n:
        return

    dfs(i+1, result)
    dfs(i+1, result + arr[i])

for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    count = 0
    dfs(0, 0)

    print(f"#{test_case} {count}")