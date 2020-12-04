with open('inputs/test.txt') as input_file:
# with open('inputs/1.txt') as input_file:
    # lines = list(input_file.read().splitlines())
    lines = input_file.read().splitlines()

# print(lines)

ans=0

passport = {}
lines.append('')
for line in lines:
    # print(line)
    line = line.strip()
    # print(line)
    if not line:
        # print(line)
        valid = all([p in passport for p in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']])
        if valid:
            ans += 1
        # print(passport, valid)
        passport = {}
    else:
        # print(line)
        params = line.split()
        # print(params)
        for param in params:
            k,v = param.split(':')
            passport[k] = v
            # print(passport)

print(ans)