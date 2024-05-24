def solution(string):
    s_arr = list(string)
    result = len(string)
    for i in range(1, len(s_arr)):
        splited = []
        for j in range(0, len(s_arr), i):
            splited.append(s_arr[j:j+i])
        t_result = ''
        for k in range(len(splited)):
            check = 1
            for l in range(k+1, len(splited)):
                if splited[k] == splited[l]:
                    check += 1
                else:
                    break
            if 1 < check:
                if len(t_result) == 0:
                    t_result += str(check)
                    continue
                if t_result[-1].isdigit():
                    continue
                else:
                    t_result += str(check)
            else:
                t_result += ''.join(splited[k])
        result = min(result, len(t_result))
    return result
print(solution('abcabcabcabcdededededede'))