T = int(input())

for test_case in range(1, T + 1):
    test_n = int(input())

    value = -1
    prev_value = -1
    count = 0
    prev_count = 0

    grades = sorted(list(map(int, input().split())))
    
    for g in grades:
        if g == value:
            count += 1
        if g != value:
            value = g
            count = 1
        if prev_count <= count and prev_value <= value:
            prev_count = count
            prev_value = value
            
            
    print(f"#{test_n}{prev_value}")