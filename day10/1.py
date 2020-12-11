# with open('inputs/test.txt') as input_file:
# with open('inputs/test2.txt') as input_file:
with open('inputs/1.txt') as input_file:
    lines = list([int(line) for line in input_file.read().splitlines()])

# print(lines)

lines.append(0)
lines = sorted(lines)
lines.append(max(lines)+3)
print(lines)
d1 = 0
d3 = 0
for i in range(len(lines)-1):
    d = lines[i+1] - lines[i]
    if d == 1:
        d1 +=1
    elif  d==3:
        d3 += 1

print(d1, d3, d1*d3)