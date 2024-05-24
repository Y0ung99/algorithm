import itertools
def solution(n, weak, dist):
    length = len(weak)
    weak = weak + list(map(lambda x: x + n, weak))
    ans = len(dist) + 1
    for start in range(length):
        for perm in itertools.permutations(dist):
            cnt = 1
            position = weak[start] + perm[cnt-1]
            for i in range(start, start + length):
                if position < weak[i]:
                    cnt += 1
                    if cnt > len(dist):
                        break
                    position = weak[i] + perm[cnt-1]
            ans = min(ans, cnt)
    if ans > len(dist):
        return -1
    return ans

print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))
print(solution(12, [1, 3, 4, 9, 10], [3, 5, 7]))
