import sys

n = int(input())
arr = list(map(int, sys.stdin.readline().split()))
add, sub, mul, div = map(int, sys.stdin.readline().split())
MAX = -1e9
MIN = 1e9
def dfs(i, hap):
    global MAX, MIN, add, sub, mul, div
    if i == n:
        MAX = max(MAX, hap)
        MIN = min(MIN, hap)
    else:
        if add > 0:
            add -= 1
            dfs(i + 1, hap + arr[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i + 1, hap - arr[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i + 1, hap * arr[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i + 1, int(hap / arr[i]))
            div += 1
dfs(1, arr[0])
print(MAX)
print(MIN)