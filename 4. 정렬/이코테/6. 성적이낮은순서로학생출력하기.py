n = int(input())
arr = []
for _ in range(n):
    name, score = map(str, input().split())
    arr.append((name, int(score)))
arr.sort(key=lambda x: x[1])
print(' '.join(map(lambda x: x[0], arr)))