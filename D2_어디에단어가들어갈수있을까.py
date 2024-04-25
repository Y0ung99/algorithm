T = int(input())

def bfs(arr, x, y, d, l):
    global count

    dx = [1, 0]
    dy = [0, 1]

    if l == k:
        if d == 0:
            cx = [x + 1, x - l]
            for c in cx:
                if 0 <= c < n:
                    if arr[c][y] == 1:
                        return
        elif d == 1:
            cy = [y + 1, y - l]
            for c in cy:
                if 0 <= c < n:
                    if arr[x][c] == 1:
                        return
        count += 1

    nx = x + dx[d]
    ny = y + dy[d]

    if 0 <= nx < n and 0 <= ny < n:
        if arr[nx][ny] == 1:
            bfs(arr, nx, ny, d, l+1)
    return

for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    arr = []
    count = 0
    for _ in range(n):
        arr.append(list(map(int, input().split())))

    for x in range(n):
        for y in range(n):
            if arr[x][y] == 1:
                bfs(arr, x, y, 0, 1)
                bfs(arr, x, y, 1, 1)
    print(f"#{test_case} {count}")


