T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    stu = []
    for _ in range(n):
        stu.append(tuple(map(int, input().split())))
    cor = [0] * 201

    for s in stu: # 1
        x, y = s[0], s[1]
        if x % 2 == 1:
            x += 1
        if y % 2 == 1:
            y += 1
        x = x // 2
        y = y // 2
        if x > y:
            x, y = y, x

        for i in range(x, y+1):
            cor[i] += 1

    print(f"#{test_case} {max(cor)}")
