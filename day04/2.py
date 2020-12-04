# with open('inputs/test3.txt') as input_file:
with open('inputs/1.txt') as input_file:
    lines = input_file.read().splitlines()

# print(lines)

p1=0
p2=0

passport = {}

def in_range(p, min,max):
    return min<=int(p)<=max

lines.append('')
for line in lines:
    line = line.strip()
    # print(line)
    if not line:
        valid1 = all([p in passport for p in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']])
        if valid1:
            p1 += 1
            valid2 = True

            if not in_range(passport['byr'], 1920, 2002):
                valid2 = False

            if not in_range(passport['iyr'], 2010, 2020):
                valid2 = False

            if not in_range(passport['eyr'], 2020, 2030):
                valid2 = False
            
            height = passport['hgt']
            # print(height[-2:])
            if height[-2:]=='in':
                # print(height)
                # print(height[:2])
                # print(height[:-2])
                if not in_range(height[:-2], 59, 76):
                    valid2 = False
            elif height[-2:]=='cm':
                if not in_range(height[:-2], 150, 193):
                    valid2 = False
            else:
                # print(height)
                valid2 = False

            hair = passport['hcl']
            # print(hair)
            # print(hair[1:])
            if len(hair[1:]) != 6 or hair[0]!='#' or any(color not in '0123456789abcdef' for color in hair[1:]):
                valid2 = False

            eye = passport['ecl']
            if eye not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                valid2= False

            passid = passport['pid']
            if len(passid) != 9 or any(x not in '0123456789' for x in passid):
                valid2 = False

            if valid2:
                p2 += 1
        passport = {}
    else:
        params = line.split()
        for param in params:
            k,v = param.split(':')
            passport[k] = v

print('Part 1:', p1)
print('Part 2:', p2)