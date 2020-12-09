from copy import deepcopy

# with open('inputs/test.txt') as input_file:
with open('inputs/1.txt') as input_file:
    # lines = input_file.read().splitlines()
    lines = [l.split() for l in input_file.read().splitlines()]

# print(lines)

def run(instructions, ip, acc):
    # instruction = instructions[ip].split()
    instruction = instructions[ip]
    if instruction[0] == 'acc':
        acc += int(instruction[1])
        ip += 1
    elif instruction[0] == 'nop':
        ip += 1
    elif instruction[0] == 'jmp':
        ip += int(instruction[1])
    return(ip, acc)

i = 0
acc = 0
seen = set()
while True:
    if i in seen:
        print('Part 1:', acc)
        break
    seen.add(i)
    i, acc = run(lines, i, acc)

for change in range(len(lines)):
    # new_lines = list(lines)
    new_lines = deepcopy(lines)
    # print(new_lines)
    # print(len(new_lines))
    # print(new_lines[change][0])
    if new_lines[change][0] == 'nop':
        new_lines[change][0] = 'jmp'
    elif new_lines[change][0] == 'jmp':
        new_lines[change][0] = 'nop'
    else:
        continue
    t = 0
    i = 0
    acc = 0
    while 0 <= i < len(new_lines) and t < 1000:
        t += 1
        i, acc = run(new_lines, i, acc)
        # print(i, acc)
    if i == len(new_lines):
        print('Part 2:', acc)