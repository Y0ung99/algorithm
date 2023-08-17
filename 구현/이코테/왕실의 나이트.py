ipt = input()
sets = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}
pos = []
ways = 0

pos.append(sets[ipt[0]])
pos.append(int(ipt[1]))

if pos[0] + 1 <= 8 and pos[1] + 2 <= 8:
    ways += 1
if pos[0] + 2 <= 8 and pos[1] + 1 <= 8:
    ways += 1
if pos[0] - 1 >= 1 and pos[1] - 2 >= 1:
    ways += 1
if pos[0] - 2 >= 1 and pos[1] - 1 >= 1:
    ways += 1
if pos[0] - 2 >= 1 and pos[1] + 1 <= 8:
    ways += 1
if pos[0] + 2 <= 8 and pos[1] - 1 >= 1:
    ways += 1
if pos[0] - 1 >= 1 and pos[1] + 2 <= 8:
    ways += 1
if pos[0] + 1 <= 8 and pos[1] - 2 >= 1:
    ways += 1

print(ways)