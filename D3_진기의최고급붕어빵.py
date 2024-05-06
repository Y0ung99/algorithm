T = int(input())
# 모든 손님에 대해 기다리는 시간이 없이 붕어빵을 제공할 수 있으면 “Possible”을, 아니라면 “Impossible”을 출력한다.

for test_case in range(1, T + 1):
    n, m, k = map(int, input().split()) # n명의사람 m초에 k개씩 붕어빵
    serve = list(map(int, input().split())) # n명의 도착 시간
    serve.sort()
    result = 'Possible'

    for i in range(n):
        b = (serve[i] // m) * k - (i+1)
        # (serve[i] // m) * k -> 도착시간에 따른 붕어빵개수
        # i+1 빼는 이유 -> 오름차순으로 정렬했기 때문에 먼저 가져간 사람도 붕어빵 개수를 뺌
        if b < 0:
            result = 'Impossible'
            break

    print(f"#{test_case} {result}")
