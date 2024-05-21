def f_way(arr, x, y):
    global t_way
    arr[x][y] = 2

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 16 and 0 <= ny < 16:
            if arr[nx][ny] == 0:
                f_way(arr, nx, ny)
            elif arr[nx][ny] == 3:
                t_way = 1
                return

for test_case in range(1, 11):
    n = int(input())
    t_way = 0
    miro = []
    for _ in range(16):
        miro.append(list(map(int, list(input()))))
    f_way(miro, 1, 1)

    print(f"#{test_case} {t_way}")


