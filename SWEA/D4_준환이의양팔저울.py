from itertools import permutations
T = int(input())
def put(o, left, right, limit): # order = 4 2 1, [], [], 0
    global result

    if limit == n:
        result += 1
        return

    if left > s_w // 2:
        N = n - limit
        result += (2 ** N)
        return

    put(order, left + o[limit], right, limit + 1)

    if left >= right + o[limit]:
        put(order, left, right + o[limit], limit + 1)

for test_case in range(1, T+1):
    n = int(input())
    chu = list(map(int, input().split()))
    result = 0
    s_w = sum(chu)

    for order in permutations(chu, n):
        put(order, 0, 0, 0)

    print(f"#{test_case} {result}")