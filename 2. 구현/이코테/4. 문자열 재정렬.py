s = list(input())
s.sort()
m = 0
for _s in s:
    if _s.isdigit():
        m += 1
    else:
        break
right = str(sum(list(map(int, list(s[:m])))))
left = ''.join(s[m:])
print(left + right)