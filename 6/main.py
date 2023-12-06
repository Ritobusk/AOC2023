f = list(map(lambda line: 
            list(map(lambda x: int(x), 
                    line.split(":")[1].strip().split())), 
             open("in.in").readlines()))
f2 = list(map(lambda line: 
                    int(line.split(":")[1].strip().replace(" ", "")), 
             open("test.in").readlines()))
print(f)
print(f2)

time = f[0]
distances = f[1]
time2 = f2[0]
distances2 = f2[1]

total = 1
total2 = 1

for i, t in enumerate(time):
    betters = 0
    for milipersec in range(1, t+1):
        tmp = (t - milipersec) * milipersec
        if tmp > distances[i]: betters += 1
    if betters > 0: total *= betters
    print(betters)



betters = 0
for milipersec in range(1, time2+1):
    tmp = (time2 - milipersec) * milipersec
    if tmp > distances2: betters += 1
if betters > 0: total2 *= betters
print(betters)


print(total)
print(total2)
