#1
s = input()
i = 0

one = 0
zero = 0

while i < len(s)-1:
    if s[i] == '1' and s[i+1] == '0':
        one += 1
    if s[i] == '0' and s[i+1] == '1':
        zero += 1
    i += 1

if s[len(s) - 2] == 0:
    one += 1
else:
    zero += 1

print(min(one, zero))