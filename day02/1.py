from collections import defaultdict

# with open('inputs/test.txt') as input_file:
with open('inputs/1.txt') as input_file:
    lines = list(input_file.read().splitlines())

# print(lines)

ans = 0

for line in lines:
    pass_with_req = line.strip().split()
    min,max = [int(x) for x in pass_with_req[0].split('-')]
    req_char = pass_with_req[1][0]
    password = pass_with_req[2]

    # print(min,max, req_char, password, pass_with_req)

    # Defining the dict 
    # d = defaultdict(int)
   
    # L = [1, 2, 3, 4, 2, 4, 1, 2] 
   
    # Iterate through the list 
    # for keeping the count 
    # for i in L:  
    # The default value is 0 
    # so there is no need to  
    # enter the key first 
    # d[i] += 1
       
    # print(d)
    # defaultdict(<class 'int'>, {1: 2, 2: 3, 3: 1, 4: 2})

    counter = defaultdict(int)
    for char in password:
        counter[char] +=1
    # print(counter)
    if min <= counter[req_char] <= max:
        ans += 1
print(ans)