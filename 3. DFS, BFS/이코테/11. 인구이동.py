from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def grouping(visited, _x ,_y):
    q = deque([(_x, _y)])
    _q = deque([(_x, _y)])
    visited[_x][_y] = True
    population = 0
    while q:
        __x, __y = q.popleft()
        population += arr[__x][__y]
        for i in range(4):
            nx = __x + dx[i]
            ny = __y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny]:
                    if l <= abs(arr[__x][__y] - arr[nx][ny]) <= r:
                        visited[nx][ny] = True
                        q.append((nx, ny))
                        _q.append((nx, ny))
    if population:
        population //= len(_q)
        while _q:
            x, y = _q.popleft()
            arr[x][y] = population

n, l, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
cnt = 0

while True:
    visited = [[False] * n for _ in range(n)]
    check = 0
    for x in range(n):
        for y in range(n):
            if not visited[x][y]:
                grouping(visited, x, y)
                check += 1
    if check == n**2:
        break
    cnt += 1

print(cnt)