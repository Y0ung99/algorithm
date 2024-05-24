order = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}
n = int(input())
plan = list(input().split())
x, y = 0, 0
for p in plan:
    dx, dy = order[p]
    nx = x + dx
    ny = y + dy
    if 0 <= dx < n and 0 <= dy < n:
        x = nx
        y = ny
print(x+1, y+1)