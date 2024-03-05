def is_num(c):
    try:
        float(c)
        return True
    except ValueError:
        return False
    
s = input()
strs = []
nums = 0

for c in s:
    if is_num(c):
        nums += int(c)
    else:
        strs.append(c)

print(''.join(sorted(strs)) + str(nums))