import heapq
def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i+1))

    sum_value = 0
    previous_food = 0
    length = len(food_times)
    while sum_value + ((q[0][0] - previous_food) * length) <= k:
        now_food = heapq.heappop(q)[0]
        sum_value += (now_food - previous_food) * length
        length -= 1
        previous_food = now_food
    result = sorted(q, key=lambda x: x[1])
    return result[(k-sum_value) % length][1]

print(solution( [4, 2, 3, 6, 7, 1, 5, 8], 16))