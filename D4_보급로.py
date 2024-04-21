from collections import deque

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    graph = []
    q = deque()
    pos_x = 0
    pos_y = 0
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0 , -1]
    foot_step = [[10000] * n for _ in range(n)]

    for i in range(n):
        graph.append([])
        ipt = input()
        for c in ipt:
            graph[i].append(int(c))

    q.append((pos_x, pos_y, 0))

    while q:
        x, y, s = q.popleft()
            
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx < n and 0 <= ny < n) and ((s + graph[nx][ny]) < (foot_step[nx][ny])):
                q.append((nx, ny, s + graph[nx][ny]))
                foot_step[nx][ny] = s + graph[nx][ny]
    print(f"#{test_case} {foot_step[n-1][n-1]}")
    
            
        


    
    