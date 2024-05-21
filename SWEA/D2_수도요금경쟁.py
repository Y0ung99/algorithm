T = int(input())

for test_case in range(1, T + 1):
    p, q, r, s, w = map(int, input().split())

    A = w * p
    B = 0
    if w < r:
        B = q
    elif w >= r:
        B = q + (w-r) * s
    print(f"#{test_case} {min(A, B)}")
