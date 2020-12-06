# with open('inputs/test.txt') as input_file:
with open('inputs/1.txt') as input_file:
    lines = input_file.read().splitlines()

# print(lines)

p1 = 0
p2 = 0

alphabet = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}

any_yes = set()
all_yes = set(alphabet)

# print(all_yes)

lines.append('')
for line in lines:
    line = line.strip()
    if not line:
        # print(yes)
        p1 += len(any_yes)
        p2 += len(all_yes)
        any_yes = set()
        all_yes = set(alphabet)
    else:
        for char in line:
            any_yes.add(char)

        for char in alphabet:
            if char not in line and char in all_yes:
                all_yes.remove(char)

print('Part 1:', p1)
print('Part 2:', p2)