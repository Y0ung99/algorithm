import itertools

T = int(input())

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
def connect(_order):
    global connected_processor
    connected = 0
    maximized_connector = []
    for _or in itertools.permutations(_order):
        temp_p = [cloned_processor[tq][:] for tq in range(n)]
        connecting = 0
        for a, b in _or:
            wiring = n ** 2
            ox = -1
            oy = -1
            d = -1
            for _i in range(4):
                nx = a + dx[_i]
                ny = b + dy[_i]
                wire = 0
                while (0 <= nx < n and 0 <= ny < n) and temp_p[nx][ny] == 0:
                    wire += 1
                    nx += dx[_i]
                    ny += dy[_i]
                if not (0 <= nx < n and 0 <= ny < n):
                    if wire < wiring:
                        wiring = wire
                        ox = nx
                        oy = ny
                        d = _i
            if d > -1 and wiring != n ** 2:
                connecting += 1
                for __i in range(wiring):
                    ox -= dx[d]
                    oy -= dy[d]
                    temp_p[ox][oy] = 3
        if connecting > connected:
            connected = connecting
            maximized_connector = [temp_p[_mc][:] for _mc in range(n)]

    connected_processor += connected

    if maximized_connector:
        return maximized_connector
    else:
        return cloned_processor

for test_case in range(1, T + 1):
    n = int(input())
    processor = [list(map(int, input().split())) for _ in range(n)]
    cloned_processor = [processor[_rs][:] for _rs in range(n)]
    connected_processor = 0
    line = 0

    for i in range(n):
        order = []
        x = i
        _x = n - i - 1

        for y in range(i, n - i):
            if processor[x][y] == 1:
                order.append((x, y))
            if processor[y][x] == 1:
                order.append((y, x))
            if processor[_x][y] == 1:
                order.append((_x, y))
            if processor[y][_x] == 1:
                order.append((y, _x))

        order = set(order)
        if i == 0:
            connected_processor += len(order)
            continue

        cloned_processor = connect(order)

    for t in cloned_processor:
        line += t.count(3)

    print(f"#{test_case} {line}")