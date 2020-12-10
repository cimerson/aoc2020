with open('inputs/test.txt') as input_file:
# with open('inputs/1.txt') as input_file:
    # lines = input_file.read().splitlines()
    lines = list([int(line) for line in input_file.read().splitlines()])

# print(lines)

invalid = 127
# invalid = 50047984

# lines.append('')
for i in range(len(lines)):
    sumn = lines[i]
    minn = lines[i]
    maxn = lines[i]
    for j in range(i+1, len(lines)):
        sumn += lines[j]
        minn = min(lines[j], minn)
        maxn = max(lines[j], maxn)
        if sumn == invalid:
            print(sumn)
            print(i, j, lines[i:j+1])
            print(minn,maxn, minn+maxn)