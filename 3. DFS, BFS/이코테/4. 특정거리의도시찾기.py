from collections import deque
import sys

n, m, k, x = map(int, input().split())

paths = [[] for _ in range(n+1)]
distance = [-1] * (n+1)
distance[x] = 0

for _ in range(m):
    ipt = list(map(int, sys.stdin.readline().split()))
    paths[ipt[0]].append(ipt[1])

queue = deque([x])

while queue:
    v = queue.popleft()
    for path in paths[v]:
        if distance[path] == -1:
            distance[path] = distance[v] + 1
            queue.append(path)
    
check = False
for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        check = True
if check == False:
    print(-1)