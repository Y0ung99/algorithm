T = int(input())
def dfs(v, s):
    global max_line
    for i in graph[v]:
        if not visited[i]:
            visited[i] = True
            dfs(i, s+1)
    visited[v] = False
    if max_line < s:
        max_line = s

for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    max_line = 0

    for _ in range(m):
        x, y = map(int, input().split())
        graph[x-1].append(y-1)
        graph[y-1].append(x-1)

    for v in range(n):
        visited = [False for _ in range(n)]
        dfs(v, 0)

    print(f"#{test_case} {max_line}")