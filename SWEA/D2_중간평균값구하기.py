T = int(input())
for test_case in range(1, T + 1):
    sheet = list(map(int, input().split()))
    r = (sum(sheet) - max(sheet) - min(sheet)) / (len(sheet) - 2)
    print(f"#{test_case} {round(r)}")