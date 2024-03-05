# def solution(N, M, K):
#     answer = 0
#     time = 0
#     for _ in range(M):
#         ma = max(N)
#         index = N.index(ma)
#         if time == K:
#             temp = list(N)
#             temp[index] = 0
#             ma_1 = max(temp)
#             answer += ma_1
#             time = 0
#             print(temp)
#         else:
#             answer += ma
#             time += 1
#             print(time, ma)
#     print(answer)
        
        
# N, M, K = map(int, input().split())
# N = list(map(int, input().split()))

# solution(N, M, K)

##############################################

# K -> 중복가능횟수
# M -> 총 횟수
# K <= M
# [2, 4, 5, 4, 6] -> 배열
# 큰 수 두개 찾기
# 제일 큰 수 중복가능 횟수만큼 sum에 더하기 -> M // K -> 횟수
# 중복가능 횟수가 넘어가면 다음 큰 숫자 한번 sum에 더하기 -> M % K -> 횟수
# 합 출력

N, M, K = map(int, input().split())
arr = sorted(list(map(int, input().split())), reverse=True)
sum = 0

count = M // (K+1) * K
count += M % (K+1) 
sum += arr[0] * count
sum += arr[1] * (M-count)

print(sum)

# 부족했던점
# 반복되어 더해지는 수열의 크기를 고려하여 count를 고친다