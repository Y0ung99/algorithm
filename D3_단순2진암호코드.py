T = int(input())
guide = [[3, 2, 1, 1], [2, 2, 2, 1], [2, 1, 2, 2], [1, 4, 1, 1], [1, 1, 3, 2],
         [1, 2, 3, 1], [1, 1, 1, 4], [1, 3, 1, 2], [1, 2, 1, 3], [3, 1, 1, 2]]
def verify(_a, _p):
    t_a = _a[_p:_p+56]
    r = []
    end = 0
    for i in range(8):
        tt_a = t_a[i*7:7*(i+1)]
        decodable = []
        mark = 0
        pos = 0
        if tt_a[0] != 0:
            end = 1
            break

        for t in tt_a:
            if t == mark:
                pos += 1
            else:
                decodable.append(pos)
                mark = t
                pos = 1
        decodable.append(pos)

        if len(decodable) != 4:
            end = 1
            break

        for s, g in enumerate(guide):
            if g == decodable:
                r.append(s)
                break

    if end or len(r) != 8:
        return 0
    else:
        s_a = 0
        s_b = 0
        for f in range(8):
            if f % 2 == 0:
                s_a += r[f]
            elif f % 2 == 1:
                s_b += r[f]
        if (s_a * 3 + s_b) % 10 == 0:
            return sum(r)
        else:
            return 0

for test_case in range(1, T + 1):
    v, w = map(int, input().split())
    arr = [list(map(int, list(input()))) for _ in range(v)]
    result = 0

    for a in arr:
        if a.count(1) > 0:
            f_one = a.index(1)
            for p in range(f_one):
                t_result = verify(a, p)
                if t_result:
                    result = t_result
                    break
        if result != 0:
            break

    print(f"#{test_case} {result}")