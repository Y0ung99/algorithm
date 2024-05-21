T = int(input())

for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    na = list(map(int, input().split()))
    ma = list(map(int, input().split()))
    result = 0

    if n-m > 0:
        for i in range(n-m+1):
            t_result = 0
            temp = na[i:i+m]
            for j in range(m):
                t_result += temp[j] * ma[j]
            result = max(t_result, result)
    else:
        for i in range(m-n+1):
            t_result = 0
            temp = ma[i:i+n]
            for j in range(n):
                t_result += temp[j] * na[j]
            result = max(t_result, result)

    print(f"#{test_case} {result}")