from itertools import permutations

T = int(input())

def calc(numbers):
    x = 1
    result = 0
    for i in range(len(numbers)-1, -1, -1):
        result += x * numbers[i]
        x *= 10
    return result

def box(numbers, per, v, ex):
    if v == ex:
        return numbers
    else:
        temp = []
        for n in numbers:
            for p in per:
                n = list(n)
                t = n[:]
                t[p[0]], t[p[1]] = t[p[1]], t[p[0]]
                temp.append(t[:])
        return box(list(set(tuple(item) for item in temp)), per, v+1, ex)

for test_case in range(1, T + 1):
    numbers, ex = input().split()
    numbers = [tuple(map(int, numbers))]
    ex = int(ex)
    per = list(permutations(range(len(numbers[0])), 2))
    res_arr = list(set(tuple(item) for item in box(numbers[:], per, 0, ex)))
    print(f"#{test_case} {calc(sorted(res_arr, reverse=True)[0])}")