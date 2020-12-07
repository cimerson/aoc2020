from collections import deque

# with open('inputs/test.txt') as input_file:
with open('inputs/1.txt') as input_file:
    lines = input_file.read().splitlines()

# print(lines)

mybag = 'shinygoldbag'

mainbags = {}

for line in lines:
    line = line.strip()
    if line:
        rules = line.split()
        # print(rules)
        mainbag = rules[0]+rules[1]+rules[2]
        mainbag = mainbag[:-1]
        if rules[-3] == 'no':
            continue
        else:
            i = 4
            while i < len(rules):
                bag = rules[i]+rules[i+1]+rules[i+2]+rules[i+3]
                if bag.endswith('.'):
                    bag = bag[:-1]
                    # print(bag)
                if bag.endswith(','):
                    bag = bag[:-1]
                    # print(bag)
                if bag.endswith('s'):
                    bag = bag[:-1]
                    # print(bag)
                while any([bag.startswith(n) for n in '0123456789']):
                    bag = bag[1:]
                    # print(bag)
                # print(mainbag, bag)
                if bag not in mainbags:
                    mainbags[bag] = []
                mainbags[bag].append(mainbag)
                i += 4

seen = set()
q = deque([mybag])
while q:
    x = q.popleft()
    if x in seen:
        continue
    seen.add(x)
    for y in mainbags.get(x, []):
        q.append(y)

print(mainbags)
print(seen)
print(len(seen)-1)