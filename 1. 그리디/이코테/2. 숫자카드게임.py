# # 내 코드 #
# n, m = map(int, input().split()) # 행, 열 입력받기
# arr = [0] * n # 행개수 초기화

# for i in range(n): # 행마다
#     arr[i] = list(map(int, input().split())) # 입력받기

# answer = 0 # 답 변수 초기화

# for j in range(n): # 행별로 작은수를 찾는다
#     if answer < min(arr[j]): # 현재 값보다 행의 최소값이 더 크다면
#         answer = min(arr[j]) # 현재 값을 행의 최소값으로 변경

# print(answer) # 답 출력

"""
# 답안코드 #
n, m = map(int, input().split()) # 행, 열 입력받기

answer = 0

for i in range(n): # 행마다
    data = list(map(int, input().split())) # 입력받기
    min_value = min(data) # 현재 행에서 가장 작은 수 찾기
    answer = max(answer, min_value) # 가장 작은 수 중에서 큰 수 찾기

"""

# 한줄씩 받으면서 min 값을 구함
# 한줄마다 min값중에 제일 큰거 마지막에 출력
import math

N, M = map(int, input().split())
_min = 0

for i in range(N):
    arr = list(map(int, input().split()))
    _min = max(_min, min(arr))

print(_min)

# 부족했던점
# if문 대신에 max 함수로 바꿔쓰기