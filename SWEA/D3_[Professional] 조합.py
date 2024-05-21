mod = 1234567891
fac = [1 for _ in range(1000001)]
for i in range(1, 1000001):
    fac[i] = (fac[i-1] * i) % mod

def powFermat(num, p):
    if p == 0:
        return 1

    half = powFermat(num, p//2)

    if p % 2 == 0:
        return ((half % mod) * (half % mod)) % mod
    else:
        return (((half*num) % mod) * (half % mod)) % mod

T = int(input())

for test_case in range(1, T + 1):
    n, r = map(int, input().split())
    top = fac[n]
    bottom = (fac[n-r] % mod) * ((fac[r] % mod) % mod)
    movetoTop = powFermat(bottom, mod-2)

    print(f"#{test_case} {(top * movetoTop) % mod}")