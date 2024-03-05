n = input()
mid = (len(n) / 2)
sum1 = sum([int(v) for i, v in enumerate(n) if i < mid])
sum2 = sum([int(v) for i, v in enumerate(n) if i >= mid])

if sum1 == sum2:
    print('LUCKY')
else:
    print('READY')