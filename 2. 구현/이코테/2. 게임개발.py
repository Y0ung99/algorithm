dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
n, m = map(int, input().split())
x, y, d = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(m)]
maps[x][y] = 2
walk = 1

while True:
    flag = 0
    for i in range(d, 4+d):
        j = i % 4
        nx = x + dx[j]
        ny = y + dy[j]
        if 0 <= nx < m and 0 <= ny < n:
            if maps[nx][ny] == 0:
                maps[nx][ny] = 2
                x, y = nx, ny
                walk += 1
                d = j + 1
                flag = 1
                break

    if flag == 1:
        continue

    d -= 1
    d %= 4
    nx = x - dx[d]
    ny = y - dy[d]

    if 0 <= nx < m and 0 <= ny < n:
        if maps[nx][ny] == 2:
            x, y = nx, ny
            continue
        elif maps[nx][ny] == 1:
            break
print(walk)