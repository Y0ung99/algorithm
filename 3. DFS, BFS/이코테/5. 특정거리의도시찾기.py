import collections
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n + 1)
ans = []

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

q = collections.deque([])
for v in graph[x]:
    q.append((v, 1))
visited[x] = True

while q:
    v, c = q.popleft()
    if c == k and (not visited[v]):
        ans.append(v)
    visited[v] = True
    for e in graph[v]:
        if not visited[e]:
            q.append((e, c + 1))
if ans:
    for p in sorted(ans):
        print(p)
else:
    print(-1)