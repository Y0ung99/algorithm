from itertools import combinations

def get_homes_stores(info, n):
    homes = []
    stores = []
    for i in range(n):
        for j in range(n):
            if info[i][j] == 1:
                homes.append([i, j])
            elif info[i][j] == 2:
                stores.append([i, j])
    return homes, stores

def calc_distance(home, store):
    return abs(home[0]-store[0]) + abs(home[1]-store[1])

def calc_chicken_distance(candidate):
    chick_dis = 0
    for home in homes:
        temp_dis = 1e9
        for store in canditate:
            temp_dis = min(temp_dis, calc_distance(home, store))
        chick_dis += temp_dis
    return chick_dis

n, m = map(int, input().split())
info = []

for _ in range(n):
    info.append(list(map(int, input().split())))

homes, stores = get_homes_stores(info, n)

canditates = list(combinations(stores, m))

result = 1e9
for canditate in canditates:
    result = min(result, calc_chicken_distance(canditate))

print(result)
