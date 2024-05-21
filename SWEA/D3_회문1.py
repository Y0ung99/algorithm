for test_case in range(1, 11):
    n = int(input())
    arr = []
    count = 0
    mid = int(n / 2)

    for _ in range(8):
        arr.append(list(input()))

    for x in range(8):
        for y in range(8):
            if y + (n-1) < 8:
                temp = arr[x][y:y + n]
                check = 0
                for i in range(mid):
                    if temp[i] == temp[(len(temp) - 1) - i]:
                        check += 1
                if check == mid:
                    count += 1
            if x + (n-1) < 8:
                temp_1 = []
                for a in range(x, x + n):
                    temp_1.append(arr[a][y])
                check_1 = 0
                for i in range(mid):
                    if temp_1[i] == temp_1[(len(temp_1) - 1) - i]:
                        check_1 += 1
                if check_1 == mid:
                    count += 1

    print(f"#{test_case} {count}")