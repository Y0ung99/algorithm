# 1 정확성테스트 만족, 효율성테스트 불만족
def solution(food_times, k):
    length = len(food_times)
    pos = 0
    count = 0
    
    while 0 not in set(food_times):
        if count + length > k:
            break
        food_times = list(map(lambda x:x-1,food_times))
        count += length

    while count <= k:
            if pos == length:
                pos = 0
                
            if food_times[pos] > 0 and count < k:
                food_times[pos] -= 1
                pos += 1
                count += 1
                
            else:
                if set(food_times) == set([0]):
                    return -1
                elif count == k:
                     break
                else:
                    pos += 1
                    continue
    
    while True:
            if pos == length:
                pos = 0
            if food_times[pos]:
                return pos + 1
            else:
                pos += 1
        

print(solution([5, 4, 6, 9], 10))
print(solution([1, 1, 1, 1], 4))
print(solution([3, 1, 2], 5))


