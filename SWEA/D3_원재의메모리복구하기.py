T = int(input())

for test_case in range(1, T + 1):

    st = list(str(input()))
    result = ['0'] * (len(st))
    count = 0

    for i in range(len(st)):
        if st == result:
            break
        if st[i] != result[i]:
            result = result[:i] + [st[i]] * (len(st) - i)
            count += 1
    print(f"#{test_case} {count}")