def solution(N, stage):
    # 실패율 = 스테이지 도달했으나 클리어하지 못한 유저의 수 / 스테이지에 도달한 플레이어 수
    stage.sort()
    ans = []
    pos = 0
    for i in range(1, N+1):
        temp = stage[pos:]
        cant = temp.count(i)
        if cant > 0:
            pos += cant
            fail_v = cant / len(temp)
            ans.append((i, fail_v))
        else:
            ans.append((i, 0))
    ans.sort(key=lambda x: x[1], reverse=True)
    return list(map(lambda x: x[0], ans))

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4, 4, 4, 4, 4]))