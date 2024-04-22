n = int(input())

for i in range(1, n+1):
    temp = []
    for c in str(i):
        if c == '3' or c == '6' or c == '9':
            temp.append('-')
        else:
            temp.append(c)
    if temp.count('-'):
        for i, t in enumerate(temp):
            if t.isdigit():
                temp[i] = ''
    print(''.join(temp), end=' ')
        