T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    area = []
    for _ in range(n):
        temp = list(map(int, list(input())))
        area.append(temp)

    m = int(n / 2)
    result = 0

    for i in range(1,m+1):
        result += sum(area[m+i][i:n-i])
    for j in range(m, 0, -1):
        result += sum(area[m-j][j:n-j])
    result += sum(area[m])

    print(f"#{test_case} {result}")