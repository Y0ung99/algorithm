from collections import deque
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
limit, last_x, last_y = map(int, input().split())
virus = []
for x in range(n):
    for y in range(n):
        if arr[x][y] != 0:
            virus.append((x, y, arr[x][y], 0))
virus.sort(key=lambda x: x[2])
q = deque(virus)

while q:
    x, y, c, t = q.popleft()
    if t == limit:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if arr[nx][ny] == 0:
                arr[nx][ny] = c
                q.append((nx, ny, c, t+1))
print(arr[last_x-1][last_y-1])