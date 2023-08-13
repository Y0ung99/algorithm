n, k = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr.sort(reverse=True)

coin = 0

for c in arr:
    if c <= k:
        coin += k // c
        k %= c
    if k == 0:
        break

print(coin)