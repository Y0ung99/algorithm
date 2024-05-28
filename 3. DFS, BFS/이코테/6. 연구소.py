import itertools
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
def dfs(_t, _x, _y):
    for i in range(4):
        nx = _x + dx[i]
        ny = _y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if _t[nx][ny] == 0:
                _t[nx][ny] = 2
                dfs(_t, nx, ny)

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
blank = []
virus = []
safe = 0
for x in range(n):
    for y in range(m):
        if arr[x][y] == 0:
            blank.append((x, y))
        if arr[x][y] == 2:
            virus.append((x, y))

for fill in itertools.combinations(blank, 3):
    temp = [arr[x][:] for x in range(n)]
    for f_x, f_y in fill:
        temp[f_x][f_y] = 1
    for v_x, v_y in virus:
        dfs(temp, v_x, v_y)
    safe = max(safe, sum([temp[x].count(0) for x in range(n)]))

print(safe)