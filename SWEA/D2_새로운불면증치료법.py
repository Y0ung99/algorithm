T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    i = 1
    result = []
    while len(result) != 10:
        t_s = list(str(n*i))
        for t in t_s:
            if result.count(t) == 0:
                result.append(t)
        i += 1
    print(f"#{test_case} {(i-1) * n}")