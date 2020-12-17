import re

# with open('inputs/test.txt') as input_file:
with open('inputs/1.txt') as input_file:
    # lines = input_file.read().splitlines()
    lines = [l.strip() for l in input_file.read().splitlines()]

# print(lines)

scanning = False
limits = []
res = 0
for line in lines:
    # print(line)
    if scanning:
        valuetikets = [int(x) for x in line.split(',')]
        # print(valuetikets)
        for value in valuetikets:
            valid = False
            for a,b,c,d in limits:
                if a<=value<=b or c<=value<=d:
                    valid = True
            if not valid:
                # print(value)
                res += value
        assert len(valuetikets) == len(limits)
    else:
        valuelimits = [int(x) for x in re.findall('\d+',line)]
        # print(valuelimits)
        if len(valuelimits) == 4:
            limits.append(valuelimits)
    if 'nearby tickets:' in line:
        scanning = True

print(res)