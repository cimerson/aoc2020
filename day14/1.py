# with open('inputs/test.txt') as input_file:
with open('inputs/1.txt') as input_file:
    lines = input_file.read().splitlines()

# print(lines)
mask = ''
mem = {}
for line in lines:
    line = line.strip()
    # print(line)
    if line.startswith('mask'):
        newmask = line.split()[-1]
        # print(newmask)
        mask = newmask
    else:
        index,_,value = line.split()
        # print(line, index, value)
        index = int(index.split('[')[-1][:-1])
        value = int(value)
        newvalue = 0
        for i,bit in enumerate(reversed(mask)):
            vbit = value & (2**i)
            if bit == 'X':
                newvalue += vbit
            elif bit == '1':
                newvalue += 2**i
            elif bit == '0':
                pass
            else:
                assert False
        mem[index] = newvalue
        # print(index, newvalue)

res = 0
for k,v in mem.items():
    print(k,v)
    res += v
print(res)