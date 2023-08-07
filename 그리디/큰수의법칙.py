def solution(N, M, K):
    answer = 0
    time = 0
    for _ in range(M):
        ma = max(N)
        index = N.index(ma)
        if time == K:
            temp = list(N)
            temp[index] = 0
            ma_1 = max(temp)
            answer += ma_1
            time = 0
            print(temp)
        else:
            answer += ma
            time += 1
            print(time, ma)
    print(answer)
        
        
N, M, K = map(int, input().split())
N = list(map(int, input().split()))

solution(N, M, K)