def pow(base, exponent):
    if exponent == 0:
        return 1
    return base * pow(base, exponent-1)

# def pow_half(base, exponent):
#     if exponent == 0:
#         return 1
#
#     half = pow_half(base, exponent // 2)
#
#     if exponent % 2 == 0:
#         return half * half
#     else:
#         return base * half * half

for test_case in range(1, 11):
    t = int(input())
    n, k = map(int, input().split())
    print(f"#{t} {pow(n, k)}")
