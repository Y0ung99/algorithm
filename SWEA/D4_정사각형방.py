T = int(input())
d = [[0, 1], [0, -1], [1, 0], [-1, 0]]
def bfs(x, y):
    global cnt
    for _d in d:
        nx = _d[0] + x
        ny = _d[1] + y
        if 0 <= nx < n and 0 <= ny < n:
            if room[nx][ny] == room[x][y] + 1:
                cnt += 1
                bfs(nx, ny)

for test_case in range(1, T + 1):
    n = int(input())
    room = [list(map(int, input().split())) for _ in range(n)]
    room_n = -1
    result = 0
    for x in range(n):
        for y in range(n):
            cnt = 1
            bfs(x, y)
            if result < cnt:
                room_n = room[x][y]
                result = cnt
            elif result == cnt:
                room_n = min(room_n, room[x][y])
    print(f"#{test_case}",room_n, result)