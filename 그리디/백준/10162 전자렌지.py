def solution(t):
    origin = t
    answer = [0, 0, 0]
    btns = [300, 60, 10]

    while 1 < t:
        for i, s in enumerate(btns):
            if t - s >= 0:
                t = t - s
                answer[i] = answer[i] + 1
                break
        if t - btns[2] < 0:
            break
      
    check = answer[0] * btns[0] + answer[1] * btns[1] + answer[2] * btns[2]

    if origin == check:
        print(' '.join(list(map(str, answer))))
    else:
        print(-1)

a = int(input())
solution(a)