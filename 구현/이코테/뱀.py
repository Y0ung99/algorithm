from collections import deque

n = int(input())
board = [[0] * n for _ in range(n)]
board[0][0] = 1

k = int(input())
for _ in range(k):
    x, y = map(int, input().split())
    board[x-1][y-1] = 2

l = int(input())
plan = {}
for _ in range(l):
    t, c = input().split()
    plan[t] = c

time = 0

head_pos = [0, 0]
path = deque([[0, 0]])
direction = 'E'

def go(n, head_pos, direction):
    if direction == 'E':
        head_pos[1] += 1
    elif direction == 'S':
        head_pos[0] += 1
    elif direction == 'W':
        head_pos[1] -= 1
    elif direction == 'N':
        head_pos[0] -= 1
    
    if (0 <= head_pos[0] < n) and (0 <= head_pos[1] < n):
        return head_pos
    else:
        raise Exception('n의 값을 초과했습니다.')
    
    

def turn(direction, order):
    sets = ['E', 'S', 'W', 'N']

    if order == 'D':
        for i, s in enumerate(sets):
            if s == direction:
                if 0 <= i <= 2:
                    direction = sets[i+1]
                else:
                    direction = 'E'
                break

    elif order == 'L':
        for i, s in enumerate(sets):
            if s == direction:
                if  1 <= i <= 3  :
                    direction = sets[i-1]
                else:
                    direction = 'N'
                break
    return direction


while True:
    try:
        time += 1
        next = go(n, head_pos, direction)
        head_x = next[0]
        head_y = next[1]

        if board[head_x][head_y] == 2:
            board[head_x][head_y] = 1
            path.append([head_x, head_y])
            head_pos[0] = head_x
            head_pos[1] = head_y
        elif board[head_x][head_y] == 0:
            board[head_x][head_y] = 1
            head_pos[0] = head_x
            head_pos[1] = head_y
            path.append([head_x, head_y])
            tail = path.popleft()
            board[tail[0]][tail[1]] = 0
        elif board[head_x][head_y] == 1:
            break

        if str(time) in list(plan.keys()):
            direction = turn(direction, plan[str(time)])

    except Exception:
        break

print(time)