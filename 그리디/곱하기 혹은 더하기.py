#1
s = input()
answer = 0

for c in s:
    n = int(c)
    if 0 < n:
        if answer == 0:
            answer = 1
        answer *= n
    else:
        answer += n

print(answer)