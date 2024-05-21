s = list(map(int, list(input())))
ans = s[0]
for i in range(1, len(s)):
    if s[i] == 1 or s[i] == 0:
        ans += s[i]
    else:
        if ans == 0:
            ans = 1
        ans *= s[i]
print(ans)