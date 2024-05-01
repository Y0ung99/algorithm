T = int(input())
for test_case in range(1, T + 1):
    ratings = ['D0', 'C-', 'C0', 'C+', 'B-', 'B0', 'B+', 'A-', 'A0', 'A+']
    n, k = map(int, input().split())
    arr = []

    for _ in range(n):
        arr.append(tuple(map(int, input().split())))

    mid_t_s = list(map(lambda x: x[0] * 0.35, arr))
    end_t_s = list(map(lambda x: x[1] * 0.45, arr))
    sub_t_s = list(map(lambda x: x[2] * 0.20, arr))

    table = []
    for i in range(n):
        table.append((i+1, mid_t_s[i] + end_t_s[i] + sub_t_s[i]))

    table.sort(key=lambda x: x[1])
    term = n // 10

    for i in range(0, n, term):
        temp = table[i:i+term]
        for t in temp:
            if t[0] == k:
                print(f"#{test_case} {ratings[i // term]}")
                break

