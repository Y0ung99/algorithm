n = 1000 - int(input())
sets = [500, 100, 50, 10, 5, 1]
coin = 0

for s in sets: 
    if n // s:
        coin += n // s
        n %= s
print(coin)