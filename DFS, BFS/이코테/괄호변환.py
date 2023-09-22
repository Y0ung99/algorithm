def verify(p):
    pair = 0
    for c in p:
        if c == '(':
            pair += 1
        else:
            pair -= 1
        if pair < 0:
            return False
    return True
    
def sep(p):
    pair = 0
    u = ''
    v = ''
    for i, c in enumerate(p):
        if c == '(':
            pair += 1
        else:
            pair -= 1
        if pair == 0:
            u = p[:i+1]
            v = p[i+1:]
            break
    return u, v

def rev(p):
    r = ''
    for c in p:
        if c == '(':
            r += ')'
        if c == ')':
            r += '('
    return r

def solution(p):
    if len(p) == 0:
        return p
    if verify(p):
        return p
    
    u, v = sep(p)
    
    if verify(u):
        v_rslt = solution(v)
        return u + v_rslt
    else:
        temp = '(' + solution(v) + ')'
        temp_2 = rev(u[1:len(u)-1])
        return temp + temp_2