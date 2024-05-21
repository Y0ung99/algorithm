def dfs(la, x, y):
    global check
    dx = [0, 0, 1]
    dy = [-1, 1, 0]
    la[x][y] = 3

    for i in range(3):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 100 and 0 <= ny < 100:
            if la[nx][ny] == 1:
                dfs(la[:], nx, ny)
                break
            elif la[nx][ny] == 2:
                check = True

for test_case in range(1, 11):
    n = int(input())
    ladder = []
    for _ in range(100):
        ladder.append(list(map(int, input().split())))

    for y in range(100):
        if ladder[0][y] == 1:
            check = False
            temp = [line[:] for line in ladder]
            dfs(temp[:], 0, y)
            if check:
                print(f"#{test_case} {y}")
                break
