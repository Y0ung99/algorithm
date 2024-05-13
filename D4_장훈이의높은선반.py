# from itertools import combinations
#
# T = int(input())
# for test_case in range(1, T + 1):
#     n, b = map(int, input().split())
#     arr = list(map(int, input().split()))
#     result = b + 1
#
#     for i in range(1, n + 1):
#         for c in combinations(arr, i):
#             if sum(c) >= b and sum(c) - b >= 0:
#                 result = min(result, sum(c) - b)
#     print(f"#{test_case} {result}")

def knapsack(i, weight):
    global result
    if weight >= b and weight - b >= 0:
        result = min(result, weight - b)
    if i >= n:
        return

    knapsack(i+1, weight + arr[i])
    knapsack(i+1, weight)

T = int(input())
for test_case in range(1, T + 1):
    n, b = map(int, input().split())
    arr = list(map(int, input().split()))
    result = b + 1
    knapsack(0, 0)
    print(f"#{test_case} {result}")
