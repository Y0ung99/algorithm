T = int(input())

for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    arr = []
    for i in range(n):
        arr.append([])
        arr[i] = list(map(int, input().split()))
    max = 0
    temp = 0
    for y in range(n-m+1):
        for x in range(n-m+1):
            for f_arr in arr[y:y+m]:
                temp += sum(f_arr[x:x+m])
            if temp > max:
                max = temp
            temp = 0
    print(f"#{test_case} {max}")
            



'''
0 0
0 1
1 0
1 1

[0 0] [0 1] [0 2]
[1 0] [1 1] [1 2]
[2 0] [2 1] [2 2]
'''
