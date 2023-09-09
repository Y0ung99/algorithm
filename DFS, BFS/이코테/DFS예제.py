def dfs(graph, v, visited):
    # 현재노드를 방문처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

dfs(graph, 1, visited)

'''
dfs(1) False
    dfs(2) False
        dfs(1) False
        dfs(7) False
            dfs(2) False
            dfs(6) False
                dfs(7) False
            dfs(8) False
                dfs(1) False
                dfs(7) False
    dfs(3) False
        dfs(1) False
        dfs(4) False
            dfs(3) False
            dfs(5) False
                dfs(3) False
                dfs(4) False
        dfs(5) False
    dfs(8) False
'''