# with open('inputs/test.txt') as input_file:
with open('inputs/1.txt') as input_file:
    lines = input_file.read().splitlines()

# print(lines)

for change in range(len(lines)):
    new_lines = list(lines)
    if new_lines[change].split()[0] == 'nop':
        new_lines[change] = 'jmp ' + new_lines[change].split()[1]
    elif new_lines[change].split()[0] == 'jmp':
        new_lines[change] = 'nop ' + new_lines[change].split()[1]
    else:
        continue
    t = 0
    i = 0
    acc = 0
    while 0 <= i < len(new_lines) and t < 10000:
        t += 1
        instruction = new_lines[i].split()
        if instruction[0] == 'acc':
            acc += int(instruction[1])
            i += 1
        elif instruction[0] == 'nop':
            i += 1
        elif instruction[0] == 'jmp':
            i += int(instruction[1])
    if i == len(new_lines):
        print(acc)