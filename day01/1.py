# import sys
# import fileinput

# report =  [int(x) for x in fileinput.input()]

# with open('inputs/test.txt') as input_file:
with open('inputs/1.txt') as input_file:
    # report = input_file.read().split('\n')
    # report = input_file.read().splitlines()
    report = [int(line) for line in input_file.read().splitlines()]

# print(report)

n = len(report)

for i in range(n):
    # print(report[i])
    for j in range(i+1, n):
        # print(report[j])
        # print(report[i]+report[j])
        if report[i]+report[j]==2020:
            print(report[i], report[j], report[i]*report[j])