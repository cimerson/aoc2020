from collections import defaultdict

with open('inputs/test.txt') as input_file:
# with open('inputs/1.txt') as input_file:
    lines = [l.strip() for l in input_file.read().splitlines()]

# print(lines)

allalergents = set()
allingridients = set()

for line in lines:
    first, rest = line.split('(contains ')
    ingridients = set(first.split())
    allergens = set(rest[:-1].split(', '))
    # print(ingridients,allergens)
    allalergents |= allergens
    allingridients |= ingridients
print(allingridients, allalergents)


no = {i: set() for i in allingridients}
c = defaultdict(int)

for line in lines:
    first, rest = line.split('(contains ')
    I = set(first.split())
    A = set(rest[:-1].split(', '))
    
    for i in I:
        c[i] += 1
    
    for a in A:
        for i in allingridients:
            if i not in I:
                no[i].add(a)

# print(allalergents, no)
res = 0
for i in no:
    print(i,no[i],c[i])
    if no[i] == allalergents:
        res += c[i]
print(res)