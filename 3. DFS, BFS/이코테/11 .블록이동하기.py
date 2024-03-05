'''
N * N 의 지도에서 2 * 1 크기의 로봇을 사용함
로봇의 위치는 [0,0], [0,1]에서 시작함
로봇은 앞뒤 구분 없이 움직일 수 있음
* 오른쪽으로 움직일때 y원소 1씩 증가
* 왼쪽으로 움직일때 y원소 1씩 감소
* 아래쪽으로 움직일때 x원소 1씩 증가
* 위쪽으로 움직일때 x원소 1씩 감소

로봇의 상태가 ㅡ 상태 일때 회전 가능함 
*조건1: 왼쪽아래, 오른쪽아래가 비어있으면 시계 회전가능
*조건2: 왼쪽위, 오른쪽위가 비어있으면 반시계 회전가능
*조건3: 회전하면 ㅣ상태가됨
로봇의 위치가 [0, 0], [0, 1] 일때,
* [0, 0]을 축으로 시계방향 회전시 [1, 0], [1, 1]이 비어있어야 하고 [0, 1] -> [1, 0]
* [0, 0]을 축으로 반시계방향 회전시 [-1, 0], [-1, 1]이 비어있어야하고 [0, 1] -> [-1, 0]
* [0, 1]을 축으로 시계방향 회전시 [1, 0], [1, 1]이 비어있어야하고 [0, 0] -> [1, 1]
* [0, 1]을 축으로 반시계방향 회전시 [-1, 0], [-1, 1]이 비어있어야하고 [0, 0] -> [-1, 1]

로봇의 상태가 ㅣ 상태 일때 회전 가능함
*조건1: 왼쪽위, 왼쪽아래가 비어있으면 시계 반시계 회전가능
*조건2: 오른쪽위, 오른쪽아래가 비어있으면 시계 반시계 회전가능
*조건3: 회전하면 ㅡ 상태가 됨
로봇의 위치가 [0, 0], [1, 0] 일때,
* [0, 0]을 축으로 시계방향 회전시 [0, -1], [1, -1]이 비어있어야하고 [1, 0] -> [0, -1]  # 왼쪽위 왼쪽아래
* [0, 0]을 축으로 반시계방향 회전시 [0, 1], [1, 1]이 비어있어야하고 [1, 0] -> [0, 1] # 오른쪽위 오른쪽아래
* [1, 0]을 축으로 시계방향 회전시 [0, 1], [1, 1]이 비어있어야하고 [0, 0] -> [1, 1]  # 오른쪽위 오른쪽아래
* [1, 0]을 축으로 반시계방향 회전시 [0, -1], [1, -1]이 비어있어야하고 [0, 0] -> [1, -1] # 왼쪽위 왼쪽아래

로봇은 벽(1)이있거나 지도 밖으로 이동 불가함

'''
board = [[0, 0, 0, 0, 0, 0, 1], 
         [1, 1, 1, 1, 0, 0, 1], 
         [0, 0, 0, 0, 0, 0, 0], 
         [0, 0, 1, 1, 1, 1, 0], 
         [0, 1, 1, 1, 1, 1, 0], 
         [0, 0, 0, 0, 0, 1, 1], 
         [0, 0, 1, 0, 0, 0, 0]]

dx = [1, 0, -1, 0, -1, 1, 0, 0]
dy = [0, 1, 0, -1, 0, 0, -1, 1]
answer = []

def dfs(board, head, tail, time):
    n_head = [0, 0]
    n_tail = [0, 0]
    n = len(board)
    print(head, tail)
    if (head[0] == n-1 and head[1] == n-1) or (tail[0] == n-1 and tail[1] == n-1):
        return time
    elif time >= n * n:
        return False
    

    # 상하좌우 이동
    for i in range(8):
        print(i)
        if 4 <= i <= 5 and head[0] == tail[0]: # ㅡ 상태
            print('hi')
            n_head[0] = head[0] + dx[i]
            n_tail[0] = tail[0] + dx[i]
            n_head[1] = head[1]
            n_tail[1] = tail[1]
            queue_head = [head, n_tail]
            queue_tail = [n_head, tail]
            if 0 <= n_head[0] < n and 0 <= n_head[1] < n and 0 <= n_tail[0] < n and 0 <= n_tail[1] < n:
                for j in range(2):
                    if board[n_head[0]][n_head[1]] == 0 and board[n_tail[0]][n_tail[1]] == 0:
                        return dfs(board, queue_head[j], queue_tail[j], time+1)

        elif 6 <= i <= 7 and head[0] != tail[0]: # ㅣ 상태
            n_head[0] = head[0]
            n_tail[0] = tail[0]
            n_head[1] = head[1] + dy[i]
            n_tail[1] = tail[1] + dy[i]
            queue_head = [head, n_tail]
            queue_tail = [n_head, tail]
            if 0 <= n_head[0] < n and 0 <= n_head[1] < n and 0 <= n_tail[0] < n and 0 <= n_tail[1] < n:
                for j in range(2):
                    if board[n_head[0]][n_head[1]] == 0 and board[n_tail[0]][n_tail[1]] == 0:
                        return dfs(board, queue_head[j], queue_tail[j], time+1)
          
        n_head[0] = head[0] + dx[i]
        n_tail[0] = tail[0] + dx[i]
        n_head[1] = head[1] + dy[i]
        n_tail[1] = tail[1] + dy[i]
        if (0 <= n_head[0] < n and 0 <= n_head[1] < n) and (0 <= n_tail[0] < n and 0 <= n_tail[1] < n):
            if (board[n_head[0]][n_head[1]] == 0) and (board[n_tail[0]][n_tail[1]] == 0):
                return dfs(board, n_head, n_tail, time+1)
        
   
        
def solution(board):
    result = dfs(board, [0,0], [0,1], 0)
    return result

print(solution(board))