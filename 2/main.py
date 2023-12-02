import re
f = open("in.in").readlines()

total = 0
max_cubes = {
    "red": 12,
    "green": 13,
    "blue": 14
}


for i, line in enumerate(f):
    line = line.split(":")[1].strip()
    cubes = re.split(', |; ', line)
    print(cubes)
    game_is_good = True
    for cube in cubes:

        c = cube.split()
        if int(c[0]) > max_cubes[c[1]]:
            game_is_good = False
            break
    if game_is_good:
        total += i+1

print(total)

