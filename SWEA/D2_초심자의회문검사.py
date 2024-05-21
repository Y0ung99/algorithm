T = int(input())

for test_case in range(1, T + 1):
    s = list(input())
    mid = len(s) // 2
    check = 0
    for i in range(mid): # 0, 1  3 4
        if s[i] == s[len(s) - 1 - i]:
            check += 1
    if check == mid:
        print(f"#{test_case} {1}")
    else:
        print(f"#{test_case} {0}")