n, m = map(int, input().split())
frame = [[] for i in range(n)]

for i in range(n):
    for c in input():
        frame[i].append(int(c))

def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if frame[x][y] == 0:
        frame[x][y] = 1
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            print(frame)
            result += 1

print(result)