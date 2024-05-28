dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
def dfs(x, y):
    arr[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if arr[nx][ny] == 0:
                dfs(nx, ny)

n, m = map(int, input().split())
arr = [list(map(int, list(input()))) for _ in range(n)]
cnt = 0


for x in range(n):
    for y in range(m):
        if arr[x][y] == 0:
            dfs(x, y)
            cnt += 1
print(cnt)