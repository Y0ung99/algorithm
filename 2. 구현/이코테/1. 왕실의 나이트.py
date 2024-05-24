def atoi(a):
    if a.isnumeric():
        return int(a)
    return ord(a) - 96

dx = [1, 1, -2, 2, -1, -1, 2, -2]
dy = [2, -2, 1, 1, -2, 2, -1, -1]
x, y = map(atoi, list(input()))
cnt = 0

for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 < nx <= 8 and 0 < ny <= 8:
        cnt += 1

print(cnt)