# # 1 정확성테스트 만족, 효율성테스트 불만족
# def solution(food_times, k):
#     length = len(food_times)
#     pos = 0
#     count = 0
    
#     while 0 not in set(food_times):
#         if count + length > k:
#             break
#         food_times = list(map(lambda x:x-1,food_times))
#         count += length

#     while count <= k:
#             if pos == length:
#                 pos = 0
                
#             if food_times[pos] > 0 and count < k:
#                 food_times[pos] -= 1
#                 pos += 1
#                 count += 1
                
#             else:
#                 if set(food_times) == set([0]):
#                     return -1
#                 elif count == k:
#                      break
#                 else:
#                     pos += 1
#                     continue
    
#     while True:
#             if pos == length:
#                 pos = 0
#             if food_times[pos]:
#                 return pos + 1
#             else:
#                 pos += 1

# 책풀이
import heapq

def solution(food_times, k):
    # 전체 음식을 먹는 시간보다 k가 크거나 같다면 -1
    if sum(food_times) <= k:
        return -1
    
    # 시간이 작은 음식부터 빼야 하므로 우선순위 큐를 이용
    q = []
    for i in range(len(food_times)):
        # (음식 시간, 음식 번호) 형태로 우선순위 큐에 삽입
        heapq.heappush(q, (food_times[i], i + 1))

    sum_value = 0 # 먹기 위해 사용한 시간
    previous = 0 # 직전에 다 먹은 음식 시간
    length = len(food_times) # 남은음식 개수

    # sum_value + (현재 음식 시간 - 이전 음식 시간) * 현재 음식 개수와 k 비교
    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length
        length -= 1 # 다 먹은 음식 제외
        previous = now # 이전 음식 시간 재설정

    # 남은 음식 중에서 몇 번째 음식인지 확인하여 출력
    result = sorted(q, key=lambda x: x[1]) # 음식의 번호 기준으로 정렬
    return result[(k - sum_value) % length][1]

    '''
    0 + ((4 - 0) * 3) <= 15
    12 <= 15

    now = 4
    sum_value += (4 - 0) * 3 => 12
    length -= 1 => 2
    previous = 4

    12 + ((6 - 4) * 2) <= 15
    16 <= 15 X

    result = [[8, 1], [6, 2]]
    result[(15 - 12) % 2][1]
    result[1][1]

    '''
        

print(solution([5, 4, 6, 9], 10))
print(solution([1, 1, 1, 1], 4))
print(solution([3, 1, 2], 5))
print(solution([8, 6, 4], 15))


