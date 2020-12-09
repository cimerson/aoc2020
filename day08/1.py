import sys

# with open('inputs/test.txt') as input_file:
with open('inputs/1.txt') as input_file:
    lines = input_file.read().splitlines()

# print(lines)

i = 0
acc = 0
seen = set()
while True:
    if i in seen:
        print(acc)
        sys.exit(0)
    seen.add(i)
    instruction = lines[i].split()
    if instruction[0] == 'acc':
        acc += int(instruction[1])
        i += 1
    elif instruction[0] == 'nop':
        i += 1
    elif instruction[0] == 'jmp':
        i += int(instruction[1])