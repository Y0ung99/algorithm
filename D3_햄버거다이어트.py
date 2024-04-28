T = int(input())

for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    taste = []
    cost = []
    result = [[0] * k for _ in range(n)]

    for _ in range(n):
        t, c = map(int, input().split())
        taste.append(t)
        cost.append(c)

    for x in range(n):
        for y in range(k):
            if cost[x] <= y:
                result[x][y] = max(result[x-1][y], taste[x] + result[x-1][y-cost[x]])
            else:
                result[x][y] = result[x-1][y]

    print(f"#{test_case} {result[n-1][k-1]}")