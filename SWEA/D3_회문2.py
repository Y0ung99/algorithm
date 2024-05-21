def f_row(line):
    global ans
    global long_s
    for i in range(len(line)):
        for j in range(i, len(line)):
            temp = line[i:j]
            mid = len(temp) // 2
            check = 0
            for c in range(mid):
                if temp[c] == temp[len(temp)-c-1]:
                    check += 1
            if check == mid:
                if ans < len(temp):
                    ans = len(temp)

for test_case in range(1,11):
    n = int(input())
    arr = []
    ans = 0

    for _ in range(100):
        arr.append(list(input()))

    for x in range(100):
        f_row(arr[x])

    # 회전
    arr = [[arr[y][x] for y in range(100)] for x in range(100)]

    for x in range(100):
        f_row(arr[x])

    print(f"#{n} {ans}")
