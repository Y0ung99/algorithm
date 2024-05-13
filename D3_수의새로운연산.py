T = int(input())
arr = [[0] * 300 for _ in range(300)]
arr[0][0] = 1
i = 1
mark = 2
while i < 300:
    for _i in range(i, -1, -1):
        for _j in range(0, i + 1):
            if _i + _j == i:
                arr[_i][_j] = mark
                mark += 1
    i += 1

for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    m_r = []

    for x in range(300):
        for y in range(300):
            if arr[x][y] == n:
                m_r.append((x, y))
            if arr[x][y] == k:
                m_r.append((x, y))
                if len(m_r) == 2:
                    break
        if len(m_r) == 2:
            break

    print(f"#{test_case} {arr[m_r[0][0] + m_r[1][0]+1][m_r[0][1] + m_r[1][1]+1]}")