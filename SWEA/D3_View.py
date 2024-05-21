for test_case in range(1, 11):
    n = int(input())
    bulidings = list(map(int, input().split()))
    nice_view_n = 0

    for i in range(2, n-2):
        left_1 = bulidings[i] - bulidings[i-2]
        left_2 = bulidings[i] - bulidings[i-1]
        right_1 = bulidings[i] - bulidings[i+1]
        right_2 = bulidings[i] - bulidings[i+2]

        left_min = min(left_1, left_2)
        right_min = min(right_1,right_2)

        if left_min < 0 or right_min < 0:
            continue
        nice_view_n += min(left_min, right_min)

    print(f"#{test_case} {nice_view_n}")
        



