s = input()
arr = []
temp = ''

for c in s:
    if c == '-':
        arr.append(int(temp))
        arr.append('-')
        temp = ''
    elif c == '+':
        arr.append(int(temp))
        arr.append('+')
        temp = ''
    else:
        temp += c
arr.append(int(temp))


for i in range(1, len(arr), 2):
    if arr[i] == '+':
        arr[i+1] = arr[i-1] + arr[i+1]
        arr[i-1] = 0
        arr[i] = 0

arr = [i for i in arr if i != 0]

for i in range(1, len(arr), 2):
    if arr[i] == '-':
        arr[i+1] = arr[i-1] - arr[i+1]
        arr[i-1] = 0
        arr[i] = 0

print(arr[-1])