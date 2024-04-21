from itertools import permutations

T = int(input())

def change(numbers, a, b):
    temp = numbers[a]
    numbers[a] = numbers[b]
    numbers[b] = temp
    return numbers

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
                temp.append(change(n[:], p[0], p[1]))
        return box(temp[:], per, v+1, ex)
    

for test_case in range(1, T + 1):
    numbers, ex = input().split()
    numbers = [list(map(int, numbers))]
    ex = int(ex)
    per = list(permutations(range(len(numbers[0])), 2))
    res_arr = box(numbers[:], per, 0, ex)

    print(f"#{test_case} {calc(sorted(res_arr, reverse=True)[0])}")
'''
메모리 초과 오류 나중에 다시
'''