n, m = map(int, input().split())
pos = list(map(int, input().split()))
map_info = []
visit = 1
blocked = 0

for i in range(n):
    map_info.append(list(map(int, input().split())))

map_info[pos[0]][pos[1]] = 2

while True:
    if blocked == 4:
        if pos[2] == 0:
            if map_info[pos[0] + 1][pos[1]] == 1 or pos[0] + 1 >= n:
                break
            else:
                pos[0] += 1
                blocked = 0
        elif pos[2] == 1:
            if map_info[pos[0]][pos[1] - 1] == 1 or pos[1] - 1 < 0:
                break
            else:
                pos[1] -= 1
                blocked = 0
        elif pos[2] == 2:
            if map_info[pos[0] - 1][pos[1]] == 1 or pos[0] - 1 < 0:
                break
            else:
                pos[0] -= 1
                blocked = 0
        elif pos[2] == 3:
            if map_info[pos[0]][pos[1] + 1] == 1 or pos[1] + 1 >= m:
                break
            else:
                pos[1] += 1
                blocked = 0

    if pos[2] == 0:
        pos[2] = 3
    elif pos[2] == 1:
        pos[2] = 0
    elif pos[2] == 2:
        pos[2] = 1
    elif pos[2] == 3:
        pos[2] = 2
    
    if pos[2] == 0:
        if pos[0] - 1 >= 0 and map_info[pos[0] - 1][pos[1]] == 0:
            pos[0] -= 1
            map_info[pos[0]][pos[1]] = 2
            visit += 1
            blocked = 0
        else:
            blocked += 1
    elif pos[2] == 1:
        if pos[1] + 1 < m and map_info[pos[0]][pos[1] + 1] == 0:
            pos[1] += 1
            map_info[pos[0]][pos[1]] = 2
            visit += 1
            blocked = 0
        else:
            blocked += 1
    elif pos[2] == 2:
        if pos[0] + 1 < n and map_info[pos[0] + 1][pos[1]] == 0:
            pos[0] += 1
            map_info[pos[0]][pos[1]] = 2
            visit += 1
            blocked = 0
        else:
            blocked += 1
    elif pos[2] == 3:
        if pos[1] - 1 >= 0 and map_info[pos[0]][pos[1] - 1] == 0:
            pos[1] -= 1
            map_info[pos[0]][pos[1]] = 2
            visit += 1
            blocked = 0
        else:
            blocked += 1
    print(pos)
    print(map_info)
    print(blocked)

print(visit)
print(map_info)