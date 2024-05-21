from math import sqrt
T = int(input())

def find(parent, x):
    if parent[x] == x:
        return x
    parent[x] = find(parent, parent[x])
    return parent[x]
def union(parent, x, y, rank):
    rootX = find(parent, x)
    rootY = find(parent, y)

    if rootX == rootY:
        return
    if rank[rootX] < rank[rootY]:
        parent[rootY] = rootX
    else:
        parent[rootX] = rootY
        if rank[rootX] == rank[rootY]:
            rank[rootX] += 1
def calc_length(x, y):
    return sqrt(((y[0]-x[0])**2) + ((y[1]-x[1])**2))

for test_case in range(1, T + 1):
    n = int(input())
    gx = list(map(int, input().split()))
    gy = list(map(int, input().split()))
    e = float(input())
    graph = []
    parent = [i for i in range(n)]
    rank = [0 for i in range(n)]
    result = 0

    for x in range(n-1):
        for y in range(x+1, n):
            graph.append((x, y, (calc_length([gx[x], gy[x]], [gx[y], gy[y]]) ** 2) * e))

    graph.sort(key=lambda z: z[2])

    for g in graph:
        a, b, cost = g
        if find(parent, a) != find(parent, b):
            union(parent, a, b, rank)
            result += cost
    print(f"#{test_case} {round(result)}")