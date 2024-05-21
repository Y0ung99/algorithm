T = int(input())
def check_row_column(arr):
    for i in range(9):
        if len(set(arr[i])) == 9:
            temp = []
            for j in range(9):
                temp.append(arr[j][i])
            if len(set(temp)) != 9:
                return False
        else:
            return False
    return True
def check_3x3(arr):
    for k in range(0, 7, 3):
        for l in range(0, 7, 3):
            temp = []
            temp.append(arr[k][l:l+3])
            temp.append(arr[k+1][l:l+3])
            temp.append(arr[k+2][l:l+3])
            if len(set([y for x in temp for y in x])) != 9:
                return False
    return True

for test_case in range(1, T + 1):
    arr = []
    result = 1
    for _ in range(9):
        arr.append(list(map(int, input().split())))

    if check_row_column(arr):
        if check_3x3(arr):
            result = 1
        else:
            result = 0
    else:
        result = 0
    print(f"#{test_case} {result}")