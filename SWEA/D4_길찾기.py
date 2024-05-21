from collections import deque

for test_case in range(1, 11):
    n, k = map(int, input().split())
    ipt = list(map(int, input().split()))
    graph_1 = [0 for _ in range(100)]
    graph_2 = [0 for _ in range(100)]
    visited = [False for _ in range(100)]
    result = 0

    for i in range(1, len(ipt), 2):
        if graph_1[ipt[i-1]] == 0:
            graph_1[ipt[i-1]] = ipt[i]
        else:
            graph_2[ipt[i-1]] = ipt[i]

    q = deque([graph_1[0], graph_2[0]])

    while q:
        a = q.popleft()
        if a == 99:
            result = 1
        if visited[graph_1[a]] is False and graph_1[a] != 0:
            visited[graph_1[a]] = True
            q.append(graph_1[a])
        if visited[graph_2[a]] is False and graph_2[a] != 0:
            visited[graph_2[a]] = True
            q.append(graph_2[a])

    print(f"#{n} {result}")
