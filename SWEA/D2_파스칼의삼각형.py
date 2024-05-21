T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    pascal = [[1], [1,1]]
    for i in range(2, n):
        temp = []
        for j in range(i-1):
            temp.append(pascal[i-1][j] + pascal[i-1][j+1])
        pascal.append([1] + temp + [1])
    print(f"#{test_case}")
    for p in range(n):
        print(' '.join(map(str, pascal[p])))
