n = int(input())
arr = list(map(int, input().split()))
cnt = 0
grp = 0
for a in arr:
    cnt += 1
    if cnt >= a:
        grp += 1
        cnt = 0
print(grp)