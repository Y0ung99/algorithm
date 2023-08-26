def turned(key):
    turned_key = []
    length = len(key)
    
    for i in range(0, length, 1):
        temp = []
        for j in range(length-1, -1, -1):
            temp.append(key[j][i])
        turned_key.append(temp)
    return turned_key

def solution(key, lock):
    m = len(key)
    n = len(lock)
    hom = sum([i.count(0) for i in lock if i.count(0)])
    dol = sum([i.count(1) for i in lock if i.count(1)])
    if dol == m*m:
        return True
    
    if len(lock) < n + (m*2) - 2:
        big_lock = []
        line_plus = (((m-1)*2 + m) - n) // 2
        upper = [(n + (m*2) - 2) * [2] for i in range(line_plus)]
        lower = [(n + (m*2) - 2) * [2] for i in range(line_plus)]
        mid_l = line_plus * [2]
        mid_r = line_plus * [2]
        
        for e in lock:
            big_lock.append(mid_l+e+mid_r)
        
        lock = upper + big_lock + lower
        print(lock)

    for i in range(len(lock)):
        temp = []
        if i + m > len(lock):
            break
        for j in range(i ,i+m):
            temp.append(lock[j])

        for k in range(len(lock)-m+1):
            temp_2 = []
            for arr in temp:
                temp_2.append(arr[k:k+m])

            turn = 0
            match = 0
            dismatch = 0

            while turn < 4:
                for a in range(m):
                    for b in range(m):
                        if key[a][b] == 1 and temp_2[a][b] == 0:
                            match += 1
                        elif key[a][b] == 1 and temp_2[a][b] == 1:
                            dismatch += 1
                
                if match == hom and dismatch == 0:
                    return True

                key = turned(key)
                match = 0
                dismatch = 0
                turn += 1
            
    return False

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1 ,1 ,1], [1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 0, 1, 1, 1, 1, 1, 1], [1, 1, 1, 0, 0, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1]]))
print(solution([[0, 1], [0, 0]], [[1, 1], [0, 1]]))