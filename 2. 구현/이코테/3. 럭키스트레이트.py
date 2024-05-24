s = list(map(int, list(input())))
m = len(s) // 2
print('LUCKY') if sum(s[:m]) == sum(s[m:]) else print('READY')