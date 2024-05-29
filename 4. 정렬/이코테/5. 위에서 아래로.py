n = int(input())
arr = [int(input()) for _ in range(n)]
print(' '.join(map(str, sorted(arr, reverse=True))))