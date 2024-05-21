import random
T = int(input())
def ch_dir(x, y, d):
    if d == '<':
        ny = y - 1
        if -1 < ny:
            return [x, ny]
        else:
            return [x, c - 1]
    elif d == '>':
        ny = y + 1
        if ny < c:
            return [x, ny]
        else:
            return [x, 0]
    elif d == '^':
        nx = x - 1
        if -1 < nx:
            return [nx, y]
        else:
            return [r-1, y]
    elif d == 'v':
        nx = x + 1
        if nx < r:
            return [nx, y]
        else:
            return [0, y]

def verify(x, y, m, d):
    global fin
    if (program[x][y] == '<') or (program[x][y] == '>') or (program[x][y] == '^') or (program[x][y] == 'v'):
        nx, ny = ch_dir(x, y, program[x][y])
        verify(nx, ny, m, program[x][y])
        return
    elif program[x][y] == '_': # 메모리가 0이면 방향 오른쪽으로 바꾸기 그외면 왼쪽으로 바꾸기
        if m == 0:
            nx, ny = ch_dir(x, y, '>')
            verify(nx, ny, m, '>')
            return
        else:
            nx, ny = ch_dir(x, y, '<')
            verify(nx, ny, m, '<')
            return
    elif program[x][y] == '|': # 메모리가 0이면 방향 아래쪽으로 바꾸기 그외면 위쪽으로 바꾸기
        if m == 0:
            nx, ny = ch_dir(x, y, 'v')
            verify(nx, ny, m, 'v')
            return
        else:
            nx, ny = ch_dir(x, y, '^')
            verify(nx, ny, m, '^')
            return
    elif program[x][y] == '?': # 이동할방향 랜덤으로 바꾸기 상하좌우
        for n_v in ['<', '>', 'v', '^']:
            nx, ny = ch_dir(x, y, n_v)
            if program[nx][ny] == '@':
                fin = True
                return
        n_v = random.choice(['<', '>', 'v', '^'])
        nx, ny = ch_dir(x, y, n_v)
        verify(nx, ny, m, n_v)
        return
    elif program[x][y] == '.': # 아무것도 하지 않는다.
        nx, ny = ch_dir(x, y, d)
        verify(nx, ny, m, d)
        return
    elif program[x][y] == '@': # 프로그램을 정지한다
        fin = True
        return
    elif program[x][y] == '+': # 메모리 +1 16이상이면 0으로
        nm = m+1
        nx, ny = ch_dir(x, y, d)
        if 0 <= nm < 16:
            verify(nx, ny, nm, d)
            return
        elif 16 <= nm:
            verify(nx, ny, 0, d)
            return
    elif program[x][y] == '-': # 메모리 -1 0미만이면 15으로 변경
        nm = m-1
        nx, ny = ch_dir(x, y, d)
        if 0 <= nm < 16:
            verify(nx, ny, nm, d)
            return
        elif nm < 0:
            verify(nx, ny, 15, d)
            return
    elif program[x][y].isdigit():  # 메모리에 저장한다
        nx, ny = ch_dir(x, y, d)
        verify(nx, ny, int(program[x][y]), d)
        return
    return

for test_case in range(1, T + 1):
    r, c = map(int, input().split())
    program = []
    fin = False

    for _ in range(r):
        program.append(list(input()))

    try:
        verify(0, 0, 0, '>')
        print(f"#{test_case} YES")
    except RecursionError:
        print(f"#{test_case} NO")