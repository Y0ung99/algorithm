# 하나씩 더할때, 두개씩 더할때, n개씩 더할때 금액들 세트에 추가
# 하나씩 탐색하며 제일 작은 숫자 찾기
# 1
# from itertools import combinations

# n = int(input())
# arr = list(map(int, input().split()))
# sets = set()

# for i in range(1, n+1, 1):
#     cases = list(combinations(arr, i))
#     for s in cases:
#         sets.add(sum(s))

# for index, e in enumerate(sets):
#     if index+1 != e:
#         print(index+1)
#         break

# 책풀이
'''
#1은 애초에 그리디가 아님.
그리디 -> 현재 상태에서 매번 가장 좋아 보이는 것만을 선택하는 알고리즘
'''
# n = int(input())
# data = list(map(int, input().split))
# data.sort()

# target = 1
# for x in data:
#     #만들 수 없는 금액을 찾았을 때 반복 종료
#     if target < x:
#         break
#     target += x

# print(target)

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

target = 1
for x in arr:
    if target < x:
        break
    target += x
    print(target)
print(target)