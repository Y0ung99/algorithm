T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    temp = []
    result = []

    for _ in range(n):
        c, c_n = input().split()
        for _ in range(int(c_n)):
            temp.append(c)

    for i in range(0, len(temp)+10, 10):
        result.append(temp[i:i+10])

    print(f"#{test_case}")
    for r in result:
        if r:
            print(''.join(r))