for test_case in range(1, 11):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    arr = [[arr[x][y] for x in range(n)] for y in range(n)]
    count = 0

    for a in arr:
        for i, e in enumerate(a):
            if e == 1:
                if a[i:].count(2) < 1:
                    a[i] = 0
            if e == 2:
                if a[:i+1].count(1) < 1:
                    a[i] = 0

        temp = ''.join(map(str, a))
        temp = ''.join(temp.split('0'))
        temp = list(temp)

        t_c = 0
        for i in range(1, len(temp)):
            if temp[i - 1] == '1' and temp[i] == '2':
                t_c += 1
        count += t_c

    print(f"#{test_case} {count}")
