import collections
def balance(w):
    count = 0
    for i in range(len(w)):
        if w[i] == '(':
            count += 1
        else:
            count -= 1
        if count == 0:
            return i
def correct(w):
    count = 0
    for i in range(len(w)):
        if w[i] == '(':
            count += 1
        else:
            if count == 0:
                return False
            count -= 1
    return True
def reversing(w):
    temp = ''
    for _w in w:
        if _w == '(':
            temp += ')'
        else:
            temp += '('
    return temp

def solution(p):
    result = ''
    if p == '':
        return result
    index = balance(p)
    u = p[:index + 1]
    v = p[index + 1:]
    if correct(u):
        result = u + solution(v)
    else:
        result += '(' + solution(v) + ')' + reversing(u[1:-1])
    return result

print(solution('(()())()'))
print(solution(')('))
print(solution('()))((()'))




