import collections
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
def bfs():
    global ans
    q = collections.deque([(0, 0, 1)])
    while q:
        print(q)
        x, y, c = q.popleft()
        arr[x][y] = 0
        if x == n-1 and y == m-1:
            ans = min(ans, c)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 1:
                    q.append((nx, ny, c + 1))

n, m = map(int, input().split())
arr = [list(map(int, list(input()))) for _ in range(n)]
ans = n*m+1
bfs()
print(ans)