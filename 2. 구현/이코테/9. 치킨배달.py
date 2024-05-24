import itertools
def calc_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
home = []
chic = []
for x in range(n):
    for y in range(n):
        if arr[x][y] == 1:
            home.append((x+1, y+1))
        if arr[x][y] == 2:
            chic.append((x+1, y+1))

ans = n ** n
for i in range(1, m+1):
    for c in itertools.combinations(chic, i):
        chic_street = 0
        for h in home:
            t = n ** n
            for _c in c:
                t = min(t, calc_distance(h[0], h[1], _c[0], _c[1]))
            chic_street += t
        ans = min(chic_street, ans)
print(ans)