# #1
# s = input()
# i = 0

# one = 0
# zero = 0

# while i < len(s)-1:
#     if s[i] == '1' and s[i+1] == '0':
#         one += 1
#     if s[i] == '0' and s[i+1] == '1':
#         zero += 1
#     i += 1

# if s[len(s) - 2] == 0:
#     one += 1
# else:
#     zero += 1

# print(min(one, zero))

# 책풀이
'''
첫번째 원소를 먼저 처리하고
두번째 원소부터 모든 원소를 확인한다 (i+1이 확인하는 수, 길이 - 1)
'''
data = input()
count0 = 0 # 전부 0으로 바꾸는 경우
count1 = 0 # 전부 1로 바꾸는 경우

# 첫번째 원소에 대해서 처리
if data[0] == '1':
    count0 += 1
else:
    count1 += 1

# 두번째 원소부터 모든 원소를 확인하며
for i in range(len(data) - 1):
    if data[i] != data[i+1]: # 다음 수에서 1로 바꾸는 경우
        if data[i+1] == '1':
            count0 += 1
        else: # 다음 수에서 0으로 바뀌는 경우
            count1 += 1
            
print(min(count0, count1))