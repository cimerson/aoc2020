# with open('inputs/test.txt') as input_file:
with open('inputs/1.txt') as input_file:
    lines = input_file.read().splitlines()

# print(lines)

k1,k2 = [int(x) for x in lines]
# print(k1,k2)

def transform(x, s):
    return pow(x,s,20201227)
    # v = 1
    # for _ in range(s):
    #     v = v*x
    #     v = v%20201227
    # return v

l1 = 0
while transform(7, l1) != k1:
    l1 += 1

l2 = 0
while transform(7, l2) != k2:
    l2 += 1

encryption = transform(k1, l2)
print(l1,l2, encryption)