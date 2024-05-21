T = int(input())

def step1(c):
    temp = ''
    if c.isdigit():
        temp = str(bin(ord(c)+4))[2:]
    elif c == ' ':
        temp = str(bin(32))[2:]
    else:
        if (ord(c) - 65 > 25):
            temp = str(bin(ord(c) - 71))[2:]
        else:
            temp = str(bin(ord(c) - 65))[2:]
    return ((6 - len(temp)) *  '0') + temp
    
for test_case in range(1, T + 1):
    string = input()
    buf = ''
    result = ''
    for c in string:
        buf += step1(c)
    pos = 0
    print(f"#{test_case}", end=' ')
    while pos < len(buf):
        temp = buf[pos:pos+8]
        print(chr(int(temp, 2)), end='')
        pos += 8
    print('')
