arr = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
count = [0] * (max(arr) + 1)
for v in arr:
    count[v] += 1
for i, c in enumerate(count):
    for _ in range(c):
        print(i, end=" ")