from itertools import combinations
import copy

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
virus_poses = []
kara_poses = []

result = 0

def infection(x, y):
    if x >= 0 and x < n and y >= 0 and y < m:
        if graph[x][y] == 0:
            graph[x][y] = 2
            infection(x-1, y)
            infection(x, y-1)
            infection(x+1, y)
            infection(x, y+1)


for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            kara_poses.append([i, j])
        elif graph[i][j] == 2:
            virus_poses.append([i, j])

for wall_poses in combinations(kara_poses, 3):
    temp_graph = copy.deepcopy(graph)

    for wall_pos in wall_poses:
        graph[wall_pos[0]][wall_pos[1]] = 1

    for virus_pos in virus_poses:
        graph[virus_pos[0]][virus_pos[1]] = 0
        infection(virus_pos[0], virus_pos[1])

    zero_count = 0
    for i in range(n):
        zero_count += graph[i].count(0)

    result = max(result, zero_count)
    graph = copy.deepcopy(temp_graph)

print(result)