# with open('inputs/test.txt') as input_file:
# with open('inputs/test2.txt') as input_file:
with open('inputs/1.txt') as input_file:
    lines = list([int(line) for line in input_file.read().splitlines()])

# print(lines)

lines.append(0)
lines = sorted(lines)
lines.append(max(lines)+3)
# print(lines)
d1 = 0
d3 = 0
for i in range(len(lines)-1):
    d = lines[i+1] - lines[i]
    if d == 1:
        d1 += 1
    elif  d==3:
        d3 += 1

nwayas = {}
def dp(i):
    if i == len(lines)-1:
        return 1
    if i in nwayas:
        return nwayas[i]
    res = 0
    # print(len(lines))
    for j in range(i+1, len(lines)):
        if lines[j] - lines[i] <= 3:
            # print(dp(j))
            res += dp(j)
    nwayas[i] = res
    # print(d)
    return res

print('Part 1:', d1, d3, d1*d3)
print('Part 2:', dp(0))