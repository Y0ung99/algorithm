T = int(input())

dx = [0, 1, 0, -1, -1, 1, 1, -1]
dy = [1, 0, -1, 0, -1, 1, -1, 1]
def put(x, y, c, w, f):
    if f != -1:
        nx = x + dx[f]
        ny = y + dy[f]
        if 0 <= nx < n and 0 <= ny < n:
            if ocelo[nx][ny] != '.' and c != ocelo[nx][ny]:
                put(nx, ny, c, w+1, f)
            elif ocelo[nx][ny] == c:
                for j in range(w + 1):
                    nx -= dx[f]
                    ny -= dy[f]
                    ocelo[nx][ny] = c
    else:
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if ocelo[nx][ny] != '.' and c != ocelo[nx][ny]:
                    put(nx, ny, c, w+1, i)

for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    ocelo = []
    blank = (n - 2) // 2
    default_1 = ['.'] * blank + [2, 1] + ['.'] * blank
    default_2 = ['.'] * blank + [1, 2] + ['.'] * blank

    for i in range(n):
        if i == (n // 2 - 1):
            ocelo.append(default_1)
        elif i == (n // 2):
            ocelo.append(default_2)
        else:
            ocelo.append(['.'] * n)

    for _ in range(k):
        x, y, c = map(int, input().split())
        put(x-1, y-1, c, 0, -1)

    # for t in ocelo:
    #     print(' '.join(map(str, t)))

    black_n = sum([dot.count(1) for dot in ocelo])
    white_n = sum([dot.count(2) for dot in ocelo])

    print(f"#{test_case} {black_n} {white_n}")