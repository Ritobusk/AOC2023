import copy
cashe = {}
def count (cfg, nums):
    if cfg == "":
        return 1 if nums == () else 0
    if nums == ():
        return 0 if '#' in cfg else 1

    key = (cfg, nums)

    if key in cashe:
        return cashe[key]
    result = 0

    if cfg[0] in ".?":
        result += count(cfg[1:], nums)
    if cfg[0] in "#?":
        if nums[0] <= len(cfg) and "." not in cfg[:nums[0]] and (nums[0] == len(cfg) or cfg[nums[0]] != '#'):
            result += count(cfg[nums[0] + 1:], nums[1:])

    cashe[key] = result
    return result

total = 0

for line in open("test.in"):
    records, springs = line.strip().split()
    springs = tuple(map(int, springs.split(",")))
    total += count(records, springs)
print(total)

total2 = 0
for line in open("in.in"):
    records, springs = line.strip().split()
    springs = tuple(map(int, springs.split(",")))
    records = "?".join([records] * 5)
    springs = springs * 5
    total2 += count(records, springs)
print(total2)
