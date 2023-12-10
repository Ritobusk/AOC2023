f = open("test.in")

total = 0

for line in f:
    numbers = list(map(int, line.strip().split()))
    diff_list = []
    diff_list.append(numbers)
    i = 0
    print(numbers)
    cond = True
    while cond:
        new_diff = list(zip(diff_list[i], diff_list[i][1:len(diff_list[i])]))
        new_diff = list(map(lambda x: x[1]-x[0], new_diff))
        diff_list.append(new_diff)
        if all( [x == 0 for x in new_diff] ):
            cond = False
        else:
            i += 1
        print(diff_list) 

    new_num = 0
    for diffs in diff_list:
        new_num += diffs[-1]
    total += new_num
print(total)



