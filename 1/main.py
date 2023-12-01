f = open("in.in").readlines()

total = 0

num_3_letters = {"one" : 1, "two" : 2, "six": 6}
num_4_letters = {"four": 4, "five": 5, "nine": 9}
num_5_letters = {"three": 3, "seven" : 7, "eight": 8}

for line in f:
    num = 0
    for i in range(len(line)):
        if i > 2 and line[i-3:i] in num_3_letters:
            num += num_3_letters[line[i-3:i]] * 10
            print(line[i-3:i])
            break
        elif i > 3 and line[i-4:i] in num_4_letters:
            num += num_4_letters[line[i-4:i]] * 10
            print(line[i-4:i])
            break
        elif i > 4 and line[i-5:i] in num_5_letters:
            num += num_5_letters[line[i-5:i]] * 10
            print(line[i-5:i])
            break
        elif line[i].isdigit():
            num +=  int(line[i]) * 10
            break

    for i in reversed(range(len(line))):
        if line[i].isdigit():
            num += int(line[i])
            break
        elif i > 2 and line[i-3:i] in num_3_letters:
            num += num_3_letters[line[i-3:i]]
            print(line[i-3:i])
            break
        elif i > 3 and line[i-4:i] in num_4_letters:
            num += num_4_letters[line[i-4:i]]
            print(line[i-4:i])
            break
        elif i > 4 and line[i-5:i] in num_5_letters:
            num += num_5_letters[line[i-5:i]]
            print(line[i-5:i])
            break

    total += num
    print(num)

print(total)
