# 빈칸 위치 저장
# 선생님 위치 저장
# 학생 위치 저장

# 그래프안의 장애물 위치 빈칸에 3개 랜덤으로 배치
# 장애물 위치 바뀔때 마다 검사
# 검사 방법 -> 저장한 선생님위치 상하좌우를 전부 검사함
# 방향을 하나씩 검사하는데 검사 방향에 장애물이있으면 검사 중지
# 검사 중 학생이 있으면 다시 처음으로
# 검사 중 모든 학생이 감시를 피하면 나오고 True리턴
# 하나의 검사가 끝나면 그래프 원위치
# 모든 검사가 끝나면 False 리턴
from itertools import combinations
import copy

n = int(input())
graph = []
empty_pos = []
teachers_pos = []
students_pos = []
end = 0

def inspection_left(graph, x, y):
    if x < 0 or y < 0 or x >= n or y >= n:
        return True
    elif graph[x][y] == 'O':
        return False
    graph[x][y] = 'Y'
    return inspection_left(graph, x-1, y)

def inspection_right(graph, x, y):
    if x < 0 or y < 0 or x >= n or y >= n:
        return True
    elif graph[x][y] == 'O':
        return False
    graph[x][y] = 'Y'
    return inspection_right(graph, x+1, y)

def inspection_up(graph, x, y):
    if x < 0 or y < 0 or x >= n or y >= n:
        return True
    elif graph[x][y] == 'O':
        return False
    graph[x][y] = 'Y'
    return inspection_up(graph, x, y-1)

def inspection_down(graph, x, y):
    if x < 0 or y < 0 or x >= n or y >= n:
        return True
    elif graph[x][y] == 'O':
        return False
    graph[x][y] = 'Y'
    return inspection_down(graph, x, y+1)

for i in range(n):
    graph.append(list(input().split()))
    for j, v in enumerate(graph[i]):
        if v == 'X':
            empty_pos.append([i, j])
        elif v == 'T':
            teachers_pos.append([i, j])
        elif v == 'S':
            students_pos.append([i, j])

student_num = len(students_pos)

for empty in combinations(empty_pos, 3):
    if end == 0:
        temp = copy.deepcopy(graph)

        for pos in empty:
            temp[pos[0]][pos[1]] = 'O'

        for teacher in teachers_pos:
            x = teacher[0]
            y = teacher[1]
            left = inspection_left(temp, x, y)
            right = inspection_right(temp, x, y)
            up = inspection_up(temp, x , y)
            down = inspection_down(temp, x , y)

        check = 0
        for student in students_pos:
            if temp[student[0]][student[1]] == 'S':
                check += 1
            if check == student_num:
                end = 1
                break
    else:
        break

if end == 1:
    print('YES')
else:
    print('NO')