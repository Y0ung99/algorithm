n = int(input())
plan = list(input().split())
pos = [1, 1]

for d in plan:
    if d == 'L':
        if 1 < pos[1]:
            pos[1] -= 1
    elif d == 'R':
        if n > pos[1]:
            pos[1] += 1
    elif d == 'U':
        if 1 < pos[0]:
            pos[0] -= 1
    elif d == 'D':
        if n > pos[0]:
            pos[0] += 1

print(pos[0], pos[1])