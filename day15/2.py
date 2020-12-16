from collections import defaultdict

# test
# numbers = [2,3,1]

# input
numbers = [2,15,0,9,1,20]

spoken = defaultdict(list)

for i, n in enumerate(numbers):
    spoken[n].append(i)

# while len(numbers) != 2020:
while len(numbers) != 30000000:
    v = numbers[-1]
    l = spoken[v]
    if len(l) <= 1:
        numbers.append(0)
    else:
        diference = spoken[v][-1] - spoken[v][-2]
        numbers.append(diference)
    spoken[numbers[-1]].append(len(numbers) - 1)

print(numbers[-1])