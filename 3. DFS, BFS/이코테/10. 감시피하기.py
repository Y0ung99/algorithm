from itertools import combinations
dx = [0, 1, -1, 0]
dy = [1, 0, 0, -1]

def attack(t_a, _x, _y, d):
    global attacked
    if d == -1:
        for i in range(4):
            nx = _x + dx[i]
            ny = _y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if t_a[nx][ny] == 'S':
                    attacked = True
                    return
                elif t_a[nx][ny] == 'X' or t_a[nx][ny] == 'T':
                    t_a[nx][ny] = 'T'
                    attack(t_a, nx, ny, i)
    else:
        nx = _x + dx[d]
        ny = _y + dy[d]
        if 0 <= nx < n and 0 <= ny < n:
            if t_a[nx][ny] == 'S':
                attacked = True
                return
            elif t_a[nx][ny] == 'X' or t_a[nx][ny] == 'T':
                t_a[nx][ny] = 'T'
                attack(t_a, nx, ny, d)

n = int(input())
arr = [list(input().split()) for _ in range(n)]
t = []
s = []
x = []
ans = 'NO'

for i in range(n):
    for j in range(n):
        if arr[i][j] == 'T':
            t.append((i, j))
        elif arr[i][j] == 'S':
            s.append((i, j))
        elif arr[i][j] == 'X':
            x.append((i, j))

for comb in combinations(x, 3):
    t_arr = [arr[i][:] for i in range(n)]
    for a, b in comb:
        t_arr[a][b] = 'O'
    miss_cnt = 0
    for t_x, t_y in t:
        attacked = False
        attack(t_arr, t_x, t_y, -1)
        if not attacked:
            miss_cnt += 1
    if miss_cnt == len(t):
        ans = 'YES'
        break
print(ans)