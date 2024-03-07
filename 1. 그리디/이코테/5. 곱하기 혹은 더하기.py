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
# s = input()
# answer = 0

# for c in s:
#     n = int(c)
#     if answer == 0 or n == 0 or answer == 1 or n == 1:
#         answer += n
#     else:
#         answer *= n


# print(answer)

#3 책풀이
'''
# 첫번째문자를 대입하면 편하다.
# 조건문은 간단히
# '''
# data = input()

# #첫 번째 문자를 숫자로 변경하여 대입
# result = int(data[0])

# for i in range(1, len(data)):
#     # 두 수 중에서 하나라도 '0' 혹은 '1'인경우 더하기 수행
#     num = int(data[i])
#     if num <= 1 or result <= 1:
#         result += num
#     else:
#         result *= num

# print(result)

s = list(map(int ,list(input())))
s.sort(reverse=True)
sum = 0

for i, n in enumerate(s):
    if 1 >= n:
        sum += n
    elif sum == 0 and 1 < n:
        sum += 1
        sum *= n
    else:
        sum *= n

print(sum)