def solution(c):
    answer = [0, 0, 0, 0]
    counter = [25, 10, 5, 1]
    while 0 < c:
        for i, s in enumerate(counter):
            if c - s >= 0:
                c = c - s
                answer[i] = answer[i] + 1
                break
    print(' '.join(list(map(str, answer))))

n = int(input())

for i in range(n):
    c = int(input())
    solution(c)