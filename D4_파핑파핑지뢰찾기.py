from collections import deque

T = int(input())

dx = [0, 0, 1, -1, -1, -1, 1, 1]
dy = [1, -1, 0, 0, -1, 1, -1, 1]
def exposed(x, y):
    mine = 0
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if maps[nx][ny] == '*':
                mine += 1
    maps[x][y] = mine
def zeroAroundTostar(x, y):
    maps[x][y] = '*'
    q = deque([(x, y)])
    while q:
        a, b = q.popleft()
        for i in range(8):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if maps[nx][ny] == 0:
                    maps[nx][ny] = '*'
                    q.append((nx, ny))
                elif maps[nx][ny] != '*':
                    maps[nx][ny] = '*'



for test_case in range(1, T + 1):
    n = int(input())
    maps = []

    for _ in range(n):
        maps.append(list(input()))

    for x in range(n):
        for y in range(n):
            if maps[x][y] == '.':
                exposed(x, y)
    cnt = 0
    for x in range(n):
        for y in range(n):
            if maps[x][y] == 0:
                cnt += 1
                zeroAroundTostar(x, y)

    n_star = sum([star.count('*') for star in maps])
    print(f"#{test_case} {n*n - n_star + cnt}")