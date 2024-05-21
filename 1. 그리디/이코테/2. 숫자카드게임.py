n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
ans = 0
for a in arr:
    ans = max(min(a), ans)
print(ans)