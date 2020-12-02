# with open('inputs/test.txt') as input_file:
with open('inputs/1.txt') as input_file:
    report = [int(x) for x in input_file.read().splitlines()]

# print(report)

n = len(report)

for i in range(n):
    for j in range(i+1, n):
        if report[i]+report[j]==2020:
            print('Part 1: ', report[i], report[j], 'Answer:', report[i]*report[j])
        for k in range(j+1, n):
            if report[i]+report[j]+report[k]==2020:
                print('Part 2: ', report[i], report[j], report[k], 'Answer:', report[i]*report[j]*report[k])