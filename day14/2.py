with open('inputs/test2.txt') as input_file:
# with open('inputs/1.txt') as input_file:
    lines = input_file.read().splitlines()

# print(lines)

def memaddress(index, floating):
    if len(floating) == 0:
        return [index]
    else:
        b0 = floating[0]
        # print(b0)
        rest = floating[1:]
        # print(rest)
        res = memaddress(index,rest) + memaddress(index+2**b0, rest)
        # print(res)
        return res


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
        assert len(mask) == 36
        index,_,value = line.split()
        # print(line, index, value)
        index = int(index.split('[')[-1][:-1])
        value = int(value)
        newindex = 0
        floating = []
        for i,bit in enumerate(reversed(mask)):
            ibit = index & (2**i)
            if bit == 'X':
                floating.append(i)
                # newvalue += vbit
            elif bit == '1':
                newindex += 2**i
                # newvalue += 2**i
            elif bit == '0':
                newindex += ibit
                pass
            else:
                assert False
        # print(newindex, newvalue)
        for i in memaddress(newindex, floating):
            mem[i] = value
        print(mem)

res = 0
for k,v in mem.items():
    # print(k,v)
    res += v
print(res)