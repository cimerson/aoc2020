import re

# with open('inputs/test.txt') as input_file:
with open('inputs/1.txt') as input_file:
    # lines = input_file.read().splitlines()
    lines = [l.strip() for l in input_file.read().splitlines()]

# print(lines)

scanning = False
limits = []
res = 0
val = [[True for _ in range(20)] for _ in range(20)]
for line in lines:
    # print(line)
    if scanning:
        valuetikets = [int(x) for x in line.split(',')]
        # print(valuetikets)
        # print(len(valuetikets))
        validticket = True
        for value in valuetikets:
            valid = False
            for a,b,c,d in limits:
                if a<=value<=b or c<=value<=d:
                    valid = True
            if not valid:
                # print(value)
                res += value
                validticket = False

        if validticket:
            for i,v in enumerate(valuetikets):
                for j, (a,b,c,d) in enumerate(limits):
                    if not (a<=v<=b or c<=v<=d):
                        val[i][j] = False

        assert len(valuetikets) == len(limits)
    else:
        valuelimits = [int(x) for x in re.findall('\d+',line)]
        # print(valuelimits)
        if len(valuelimits) == 4:
            limits.append(valuelimits)
    if 'nearby tickets:' in line:
        scanning = True

print('Part 1:', res)
# print(val)
mapi = [None for _ in range(20)]
used = [False for _ in range(20)]
found = 0

while True:
    for i in range(20):
        validj = [j for j in range(20) if val[i][j] and not used[j]]
        # print(validj)
        if len(validj) == 1:
            mapi[i] = validj[0]
            used[validj[0]] = True
            found += 1
    if found == 20:
        break
print(mapi)
mine = [83,53,73,139,127,131,97,113,61,101,107,67,79,137,89,109,103,59,149,71]
p2 = 1
for i,j in enumerate(mapi):
    if j<6:
        p2 *= mine[i]
print('Part 2:', p2)