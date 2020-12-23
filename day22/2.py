from collections import deque
import re

# with open('inputs/test.txt') as input_file:
with open('inputs/1.txt') as input_file:
    lines = [l.strip() for l in input_file.read().splitlines()]

# print(lines)

d1 = deque()
d2 = deque()

p2 = False

for line in lines:
    card = line.split()
    value = re.findall('-?\d+', line)
    # print(line, card, value)
    if 'Player' in line:
        if '2' in line:
            p2 = True
    elif value:
        if p2:
            d2.append(int(value[0]))
        else:
            d1.append(int(value[0]))
# print(d1,d2)

def game(d1,d2):
    seen = set()
    while d1 and d2:
        same = (tuple(d1),tuple(d2))
        # if (d1,d2) in seen:
        if same in seen:
            return True, d1
        seen.add(same)
        # print(d1,d2)
        c1,c2 = d1.popleft(), d2.popleft()
        if len(d1)>=c1 and len(d2)>=c2:
            newd1 = deque([d1[x] for x in range(c1)])
            newd2 = deque([d2[x] for x in range(c2)])
            p1win,_ = game(newd1,newd2)
        else:
            p1win = c1>c2

        if p1win:
            d1.append(c1)
            d1.append(c2)
        else:
            d2.append(c2)
            d2.append(c1)
    if d1:
        return True,d1
    else:
        return False,d2
    
# print(d1,d2)
p1,winnerd = game(d1,d2)

score = 0
for i,c in enumerate(winnerd):
    # print(i,c)
    score += (len(d2)-i)*c
print(score)