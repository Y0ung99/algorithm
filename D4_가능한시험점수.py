T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    grade_arr = list(map(int, input().split()))
    result = [0]
    visited = [0] * (sum(grade_arr) + 1)
    visited[0] = 1
    for grade in grade_arr:
        temp_r = result[:]
        for r in temp_r:
            if r + grade < len(visited):
                if visited[r + grade] == 0:
                    visited[r + grade] = 1
                    result.append(r + grade)
    print(f"#{test_case} {len(result)}")