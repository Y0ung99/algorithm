for test_case in range(1, 11):
    n = int(input())
    f = list(input())
    st = list(input())
    cnt = 0
    for i in range(0, len(st)):
        if f == st[i:i+len(f)]:
            cnt += 1
    print(f"#{n} {cnt}")