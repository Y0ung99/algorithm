n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
dp = [10001] * (m+1)
dp[0] = 0

for a in arr:
    for j in range(a, m+1):
        dp[j] = min(dp[j], dp[j-a]+1)

print(dp[m])