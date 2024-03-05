n = int(input())

bag = 0

while n:
    # 나눠지는 경우 우선순위 1
    if n % 5 == 0:
        n -= 5
    elif n % 3 == 0:
        n -= 3

    # 뺄 수 있는 경우 우선순위 2
    elif 5 < n:
        n -= 5
    elif 3 < n < 5:
        n -= 3

    # 둘다 할 수 없는 경우 우선순위 3
    elif n < 3:
        print(-1)
        exit()

    bag += 1

print(bag)