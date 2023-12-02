import re
f = open("test.in").readlines()

total = 0
max_cubes = {
    "red": 12,
    "green": 13,
    "blue": 14
}


for i, line in enumerate(f):
    line = line.split(":")[1].strip()
    cubes = re.split(', |; ', line)
    mins = {"red": 0, "green":0,"blue":0}
    tmp = 1
    for cube in cubes:
        c = cube.split()
        if int(c[0]) > mins[c[1]]:
            mins[c[1]] = int(c[0])
    for x in mins:
        tmp *= mins[x]
    total += tmp
print(total)

