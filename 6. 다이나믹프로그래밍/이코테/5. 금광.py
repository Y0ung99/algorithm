T = int(input())

for test_case in range(T + 1):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    dp = []
    for i in range(0, n*m, m):
        dp.append(arr[i:i+m])

    for y in range(1, m):
        for x in range(n):
            left_up = 0
            left_dn = 0
            left = 0
            if 0 <= x-1 < n and 0 <= y-1 < m:
                left_up = dp[x-1][y-1]
            if 0 <= x+1 < n and 0 <= y-1 < m:
                left_dn = dp[x+1][y-1]
            if 0 <= y-1 < m:
                left = dp[x][y-1]
            dp[x][y] = dp[x][y] + max(left_up, left_dn, left)
    print(dp)

