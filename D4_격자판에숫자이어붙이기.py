T = int(input())

def bfs(arr, x, y, s):
    global result_sets
    s.append(arr[x][y])
    if len(s) == 7:
        result_sets.add(tuple(s))
        return
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 4 and 0 <= ny < 4:
            bfs(arr[:], nx, ny, s[:])


for test_case in range(1, T + 1):
    arr = []
    result = 0
    result_sets = set()

    for _ in range(4):
        arr.append(list(map(int, input().split())))

    for x in range(4):
        for y in range(4):
            bfs(arr[:], x, y,[])

    print(f"#{test_case} {len(result_sets)}")