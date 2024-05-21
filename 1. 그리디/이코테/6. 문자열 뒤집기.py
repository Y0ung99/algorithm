s = list(input())
flag = s[0]
zero = 1 if s[0] == '0' else 0
one = 1 if s[0] == '1' else 0

for i in range(1, len(s)):
    if s[i] != flag:
        print(s[i], flag)
        flag = s[i]
        zero += 1 if flag == '0' else 0
        one += 1 if flag == '1' else 0
print(min(zero, one))
