from collections import deque
def bfs(s, d):
    global D
    global result
    visited[s] = True
    q = deque([(s, d)])

    while q:
        v = q.popleft()
        if v[1] > D:
            D = v[1]
            result = [v[0]]
        elif v[1] == D:
            result.append(v[0])

        for g in graph[v[0]]:
            if not visited[g]:
                q.append((g, v[1]+1))
                visited[g] = True


for test_case in range(1, 11):
    n, s = map(int, input().split())
    ipt = list(map(int, input().split()))
    graph = [[] for _ in range(max(ipt) + 1)]
    visited = [False] * (max(ipt) + 1)
    result = []
    D = 0

    for i in range(0, n, 2):
        graph[ipt[i]].append(ipt[i + 1])

    bfs(s, 0)
    print(f"#{test_case} {max(result)}")
