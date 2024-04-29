T = int(input())

for test_case in range(1, T + 1):
    st = list(input())
    length = 0
    for i in range(2, 30):
        words = st[:i]
        nextwords = st[i:i+i]
        if words == nextwords:
            length = i
            break
    print(f"#{test_case} {length}")

