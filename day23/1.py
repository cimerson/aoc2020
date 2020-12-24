# test
# x = [int(x) for x in '389125467']

# input
x = [int(x) for x in '398254716']

t = 0
current = 0
# for _ in range(11):
for _ in range(101):
    t += 1
    print(t,x,current)
    currentval = x[current]
    pick = []
    pickidx = (current+1)%len(x)
    # pick = x[current+1:current+4]
    for _ in range(3):
        pick.append(x[pickidx])
        pickidx = (pickidx+1)%len(x)
    for i in pick:
        x.remove(i)
    assert len(pick) == 3
    assert len(pick) + len(x) == 9
    print(pick,x)

    # x = x[:current+1] + x[current+4:]

    # dest = x[current]-1
    dest = currentval-1
    if dest <= 0:
        dest = 9
    while dest in pick:
        dest -= 1
        if dest <= 0:
            dest = 9
    destidx = x.index(dest)
    # print(dest, destidx)
    # print(x)
    x = x[:destidx+1]+pick+x[destidx+1:]
    current = x.index(currentval)
    # if destidx < current:
        # current = (current+3)%len(x)
    current = (current+1)%len(x)
    # print(pick,x, current)

#2, 9, 1, 6, 7, 3, 8, 4, 5
# 67384529


    #5, 7, 9, 8, 6, 2, 3, 1, 4
    # 457986231

#5, 7, 9, 8, 6, 2, 3, 1, 4
# 45798623