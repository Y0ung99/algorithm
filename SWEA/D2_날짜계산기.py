T = int(input())
day_limit = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for test_case in range(1, T + 1):
    m, d, _m, _d = map(int, input().split())
    result = 0

    if m == _m:
        for i in range(d, _d+1):
            result += 1
    else:
        for i in range(d, day_limit[m]+1):
            result += 1
        for limit in range(m+1, _m):
            result += day_limit[limit]
        result += _d

    print(f"#{test_case} {result}")