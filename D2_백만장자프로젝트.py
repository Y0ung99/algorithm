T = int(input())
 
for test_case in range(1, T + 1):
    N = int(input())
    priceArr = list(map(int, input().split()))
    result = 0
    max_price = 0
 
    for i in range(N-1, -1, -1):
        if priceArr[i] > max_price:
            max_price = priceArr[i]
        else:
            result += max_price - priceArr[i]
 
    print(f"#{test_case} {result}")