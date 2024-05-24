import collections
def turn(s, cd):
    if s == 'L':
        return (cd - 1 + 4) % 4
    else:
        return (cd + 1 + 4) % 4

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

n = int(input())
a = int(input())

board = [[0] * n for _ in range(n)]
order = {}

for _ in range(a):
    x, y = map(int, input().split())
    board[x-1][y-1] = 5

l = int(input())
for _ in range(l):
    x, y = input().split()
    order[int(x)] = y

t = 1
d = 0
flag = 0
h_x, h_y = 0, 0
board[0][0] = 1
t_q = collections.deque([(0, 0)])

while True:
    h_x += dx[d]
    h_y += dy[d]
    if 0 <= h_x < n and 0 <= h_y < n:
        if board[h_x][h_y] == 5:
            board[h_x][h_y] = 1
            t_q.append((h_x, h_y))
        elif board[h_x][h_y] == 0:
            t_x, t_y = t_q.popleft()
            t_q.append((h_x, h_y))
            board[t_x][t_y] = 0
            board[h_x][h_y] = 1
        elif board[h_x][h_y] == 1:
            flag = 1
            break
    else:
        flag = 1
        break
    if t in order.keys():
        d = turn(order[t], d)
    t += 1
if flag:
    print(t)