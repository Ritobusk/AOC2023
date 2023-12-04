
total = 0

for line in open("in.in"):
    line = line.split(': ')[1].strip().split(' | ')
    winning_nums = -1
    winners = set(line[0].split())
    my_nums = line[1].split()
    print(winners, my_nums)
    for num in my_nums:
        if num in winners:
            winning_nums += 1

    if winning_nums > -1:
        total += pow(2, winning_nums)

print(total)
