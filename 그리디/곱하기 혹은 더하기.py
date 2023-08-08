#1 -> 1을 곱하는 경우를 생각하지 못함
# s = input()
# answer = 0

# for c in s:
#     n = int(c)
#     if 0 < n:
#         if answer == 0:
#             answer = 1
#         answer *= n
#     else:
#         answer += n

# print(answer)

#2
s = input()
answer = 0

for c in s:
    n = int(c)
    if answer == 0 or n == 0 or answer == 1 or n == 1:
        answer += n
    else:
        answer *= n


print(answer)