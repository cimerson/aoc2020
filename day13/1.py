# with open('inputs/test.txt') as input_file:
with open('inputs/1.txt') as input_file:
    lines = input_file.read().splitlines()

# print(lines)

mytime = int(lines[0])
# print(time)
buses = [int(x) for x in lines[1].split(',') if x!='x']
# print(buses)

mybus = None
for bus in buses:
    bustime = mytime
    while bustime%bus != 0:
        # print(bus, bustime)
        bustime += 1
    diference = bustime - mytime
    if mybus is None or diference < mybus[0]:
        mybus = (diference, bus)
print(mybus)
print(mybus[0]*mybus[1])
