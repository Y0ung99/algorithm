T = int(input())
def rotate_90(arr):
    temp = []
    for x in range(n):
        temp.append([])
        for y in range(n-1, -1, -1):
            temp[x].append(arr[y][x])
    return temp

for test_case in range(1, T + 1):
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))

    rotatable = []
    for _ in range(3):
        arr = rotate_90(arr)
        temp = []
        for t in arr:
            temp.append(''.join(map(str, t)))
        rotatable.append(temp)

    result = []
    for x in range(n):
        result.append([])
        for y in range(3):
            result[x].append(rotatable[y][x])

    print(f"#{test_case}")
    for r in result:
        print(' '.join(r))