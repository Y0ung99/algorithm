T = int(input())
changes = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

for test_case in range(1, T + 1):
    n = int(input())
    result = []
    for c in changes:
        result.append(n // c)
        n %= c

    print(f"#{test_case}")
    print(' '.join(map(str, result)))