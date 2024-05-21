T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    
    r_list = [[0] * n for _ in range(n)]

    check = 2
    pos_x = 0
    pos_y = 0
    dir = 'r'
    r_list[0][0] = 1

    while check <= n*n:
        if dir == 'r':
            if pos_x == n-1 or r_list[pos_y][pos_x+1]:
                dir = 'd'
                continue
            pos_x += 1
            r_list[pos_y][pos_x] = check
            
        if dir == 'd':
            if pos_y == n-1 or r_list[pos_y+1][pos_x]:
                dir = 'l'
                continue
            pos_y += 1
            r_list[pos_y][pos_x] = check
            
        if dir == 'l':
            if pos_x == 0 or r_list[pos_y][pos_x-1]:
                dir = 'u'
                continue
            pos_x -= 1
            r_list[pos_y][pos_x] = check
            
        if dir == 'u':
            if pos_y == 0 or r_list[pos_y-1][pos_x]:
                dir = 'r'
                continue
            pos_y -= 1
            r_list[pos_y][pos_x] = check
        check += 1

    print(f"#{test_case}")
    for lis in r_list:
        for l in lis:
            print(l, end=' ')
        print('')