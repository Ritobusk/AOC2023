from collections import deque
from copy import deepcopy
f = open("in.in").readlines()

seeds = []
maps = []

seeds =  list(map(lambda x: int(x), f[0].split(": ")[1].strip().split()))
seeds_ranges_s = seeds[:len(seeds):2]
seeds_ranges_e = seeds[1:len(seeds):2]
seeds_ranges = list(zip(seeds_ranges_s,seeds_ranges_e))
for i, x in enumerate(seeds_ranges):
    seeds_ranges[i] = (x[0], x[0] + x[1])
print(seeds_ranges)

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


#current_nums = seeds
##num = seeds[0]
##print(num)
#
#minimum = 100000000000000000
#for num in current_nums:
    #for a_map in maps:
        #for conversions in a_map:
            #dest = conversions[0]
            #source = conversions[1]
            #r = conversions[2]
            #if source <= num < source +r:
                #num = (dest - source) + num
                #break
        #
    #minimum = min(minimum, num)
#print(minimum)

#Part2
minimum2 = []
for seed_range in seeds_ranges:
    new_item_ranges = [seed_range]
    for a_map in maps:
        tmp_item_ranges = []
        item_queue = deque()
        for x in new_item_ranges:
            item_queue.append(x)
        print((item_queue), "hey")
        print(a_map)
        while len(item_queue) > 0:
            print((item_queue))
            items = item_queue.pop()
            for conversions in a_map:
                #print("conversion:", conversions)
                dest = conversions[0]
                source = conversions[1]
                r = conversions[2]
                converter = dest - source
                if source <= items[0] < source +r:
                    if items[1] < source + r:
                        #print("all copied",  ((converter + items[0]), (converter + items[1])) )
                        tmp_item_ranges.append( ((converter + items[0]), (converter + items[1])) )
                        break
                    else:
                        tmp_item_ranges.append( ((converter + items[0]), (converter + source + r)))
                        item_queue.append(((source + r + 1), items[1]))
                        break
                elif source <= items[1] < source + r:
                    #print("From behind")
                    #print((items[0], source - 1))
                    #print((converter + source), (converter + items[1]))
                    item_queue.append(((items[0], source)))
                    tmp_item_ranges.append(((converter + source), (converter + items[1])))
                    break
                elif items[0] <= source < items[1] and source + r < items[1]:
                    print("\n\n\n\n\n\n")
                    item_queue.append((items[0], source ))
                    item_queue.append((source + r , items[1]))
                    tmp_item_ranges.append(((converter + source), (converter + source + r)))
            #If items doesnt get changed
            else:
                print("unchanged")
                tmp_item_ranges.append(items)
                    
        new_item_ranges = deepcopy(tmp_item_ranges)
    minimum2.append(min(new_item_ranges))


print(minimum2)
print(min(minimum2))

