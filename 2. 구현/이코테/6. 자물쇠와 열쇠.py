def rotate_90(arr):
    return [[arr[y][x] for y in range(len(arr))] for x in range(len(arr)-1, -1, -1)]
def solution(key, lock):
    m = len(key)
    n = len(lock)
    z = m - 1
    space_w = z * 2 + n
    space = [[0] * space_w for _ in range(space_w)]
    for x in range(z, space_w-z):
        for y in range(z, space_w-z):
            space[x][y] = lock[x-z][y-z]

    flag = 1
    rotate = 0
    while flag:
        for x in range(space_w-z):
            for y in range(space_w-z):
                t_space = [space[x][:] for x in range(space_w)]
                for q in range(m):
                    for w in range(m):
                        t_space[x+q][y+w] += key[q][w]
                one = sum([t_space[x][z:space_w-z].count(1) for x in range(z, space_w-z)])
                if one == n**2:
                    flag = 0
                    break
            if not flag:
                break
        if rotate == 3:
            break
        key = rotate_90(key)
        rotate += 1
    if not flag:
        return 'true'
    else:
        return 'false'


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],
               [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))

