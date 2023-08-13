n = int(input())
arr = list(map(int, input().split()))
arr.sort()
temp = 0
sum = 0

for p in arr:
    temp += p
    sum += temp

print(sum)