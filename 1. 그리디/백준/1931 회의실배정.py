n = int(input())
arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

arr.sort(key=lambda x: (x[1], x[0]))

i = 1
meeting = 1
next = arr[0][1]

while i < n:
    if next <= arr[i][0]:
        next = arr[i][1]
        meeting += 1
    i += 1
    
print(meeting)