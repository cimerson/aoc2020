from collections import defaultdict

# with open('inputs/test.txt') as input_file:
with open('inputs/1.txt') as input_file:
    lines = list(input_file.read().splitlines())

# print(lines)

p1=0
p2=0

for line in lines:
    pass_with_req = line.strip().split()
    min,max = [int(x) for x in pass_with_req[0].split('-')]
    req_char = pass_with_req[1][0]
    password = pass_with_req[2]
    counter = defaultdict(int)
    for char in password:
        counter[char] +=1
    if min <= counter[req_char] <= max:
        p1 += 1
    if (password[min-1]==req_char) ^ (password[max-1]==req_char):
        p2 +=1
print('Part 1:', p1)
print('Part 2:', p2)