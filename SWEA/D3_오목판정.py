T = int(input())

dx = [0, 1, 1, 1]
dy = [1, 0, -1, 1]
def verify():
    for x in range(n):
        for y in range(n):
            if pan[x][y] == 'o':
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    cnt = 1
                    while 0 <= nx < n and 0 <= ny < n and pan[nx][ny] == 'o':
                        cnt += 1
                        nx += dx[i]
                        ny += dy[i]
                    if cnt >= 5:
                        return 'YES'
    return 'NO'


for test_case in range(1, T + 1):
    n = int(input())
    pan = [list(input()) for _ in range(n)]

    print(f'#{test_case} {verify()}')