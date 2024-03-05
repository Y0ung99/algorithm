n = int(input())
arr = []
m = 0

for _ in range(n):
    arr.append(int(input()))

arr.sort()

for i in range(0, n, 1):
    m = max(m, arr[i] * (n-i))

print(m)