def possible(answer):
    for x, y, a in answer:
        if a == 0:
            if (y == 0) or ([x, y - 1, 0] in answer) or ([x - 1, y, 1] in answer) or ([x, y, 1] in answer):
                continue
            return False
        elif a == 1:
            if (([x - 1, y, 1] in answer) and ([x + 1, y, 1] in answer)) or ([x, y - 1, 0] in answer) or ([x + 1, y - 1, 0] in answer):
                continue
            return False
    return True

def solution(n, build_frame):
    result = []
    for build in build_frame:
        x, y, a, b = build
        if b:
            result.append([x, y, a])
            if not possible(result):
                result.remove([x, y, a])
        else:
            result.remove([x, y, a])
            if not possible(result):
                result.append([x, y, a])
    return sorted(result, key=lambda x: x[0])

print(solution(5,
               [[0, 0, 0, 1], [2, 0, 0, 1],
                [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1]
                , [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0],
                [1, 1, 1, 0], [2, 2, 0, 1]]))

# print(solution(5,
#                [[1, 0, 0, 1], [1, 1, 1, 1],
#                 [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1]
#                 , [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]))

