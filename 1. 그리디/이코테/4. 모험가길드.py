# #1
# n = int(input())
# arr = list(map(int, input().split()))

# group = 0

# sets = set(arr)

# for s in sets:
#     group += arr.count(s) // s

# print(group)

# 책풀이
# n = int(input())
# data = list(map(int, input().split()))
# data.sort()

# result = 0 # 총 그룹의 수
# count = 0 # 현재 그룹에 포함된 모험가의 수

# for i in data: # 공포도 낮은 모험가 부터 하나씩 확인
#     count += 1 # 현재 그룹에 해당 모험가를 포함시키기
#     if count >= i: # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면 그룹결성
#         result += 1 # 총 그룹의 수 증가 시키기
#         count = 0 # 현재 그룹에 포함된 모험가의 수 초기화

# print(result) # 총 그룹의 수 출력

n = int(input())
arr = map(int, input().split())
arr.sort()
count = 0
group = 0

for data in arr:
    count += 1
    if count >= data:
        group += 1
        count = 0
        
print(group)