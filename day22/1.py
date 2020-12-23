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

while d1 and d2:
    c1,c2 = d1.popleft(), d2.popleft()
    if c1 > c2:
        d1.append(c1)
        d1.append(c2)
    else:
        d2.append(c2)
        d2.append(c1)
print(d1,d2)

score = 0
for i,c in enumerate(d2):
    print(i,c)
    score += (len(d2)-i)*c
print(score)