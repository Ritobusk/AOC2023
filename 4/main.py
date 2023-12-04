f = open("in.in").readlines()
total2 = [1] * len(f)
total = 0

for i, line in enumerate(f):
    line = line.split(': ')[1].strip().split(' | ')
    winning_nums = 0
    winners = set(line[0].split())
    my_nums = line[1].split()
    for num in my_nums:
        if num in winners:
            winning_nums += 1

    boards = total2[i]
        
    if winning_nums > 0:
        for j in range(1, winning_nums + 1):
            if j + i < len(f):
                total2[i+j] += boards

print(sum(total2))
