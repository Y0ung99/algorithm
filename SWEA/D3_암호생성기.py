def cycle(sec):
    temp = []
    for i in range(5):
        if sec[i] - (i+1) <= 0:
            temp.append(0)
            break
        else:
            temp.append(sec[i] - (i+1))

    t_len = len(temp) - 8
    temp = sec[t_len:] + temp[:]

    return temp

for test_case in range(1, 11):
    n = int(input())
    secret = list(map(int, input().split()))

    while secret[7] != 0:
        secret = cycle(secret)

    print(f"#{test_case} {' '.join(list(map(str, secret)))}")