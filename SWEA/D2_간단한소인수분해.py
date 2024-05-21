T = int(input())
for test_case in range(1, T + 1):
    prime = [2, 3, 5, 7, 11]
    n = int(input())
    result = []
    for p in prime:
        N = 0
        while True:
            if n % p ** N != 0:
                break
            N += 1
        n /= p ** (N - 1)
        result.append(N-1)

    print(f"#{test_case} {' '.join(map(str, result))}")