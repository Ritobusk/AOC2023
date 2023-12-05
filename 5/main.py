f = open("in.in").readlines()

seeds = []
maps = []

seeds =  list(map(lambda x: int(x), f[0].split(": ")[1].strip().split()))

one_map = []
map_prossesed = False
for line in f[1:len(f)]:
    if map_prossesed:
        maps.append(one_map)
        map_prossesed = False
        one_map = []
    if not line[0].isdigit():
        if len(one_map) > 0:
            map_prossesed = True
    elif line[0].isdigit():
        one_map.append(list(map(lambda x: int(x), line.split())))

maps.append(one_map)
print(maps)

print(seeds)

current_nums = seeds
#num = seeds[0]
#print(num)
minimum = 100000000000000000
for num in current_nums:
    for a_map in maps:
        for conversions in a_map:
            dest = conversions[0]
            source = conversions[1]
            r = conversions[2]
            if source <= num < source +r:
                print("hey", dest,source,r)
                num = (dest - source) + num
                break
        
    print(num)
    minimum = min(minimum, num)
print(minimum)



