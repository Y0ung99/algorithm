n, m, k = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort(reverse=True)
cnt = 0
ans = 0
for _ in range(m):
    if cnt != k:
        ans += arr[0]
        cnt += 1
    elif cnt == k:
        ans += arr[1]
        cnt = 0
print(ans)