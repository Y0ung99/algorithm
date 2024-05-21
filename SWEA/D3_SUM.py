for test_case in range(1, 11):
    n = int(input())
    arr = []
    m = 0
    for i in range(100):
        arr.append(list(map(int, input().split())))
        m = max(m, sum(arr[i]))

    cl = 0
    cr = 0
    for x in range(100):
        cr += arr[x][x]
        cl += arr[x][99 - x]

    print(cl, cr)
    m = max(m, cl, cr)

    for x in range(100):
        ver = 0
        for y in range(100):
           ver += arr[y][x]
        m = max(m, ver)

    print(f"#{test_case} {m}")