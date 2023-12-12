import re
space =  open("in.in").readlines()

gals = []

for row, l in enumerate(space):
    cols = [match.start() for match in re.finditer(r'#', l)]
    print(cols)
    for col in cols:
        if col != -1:
            gals.append((row, col))
print((gals))

empty_rows = []
empty_cols = []
max_row = max(gals, key=lambda x: x[0])
max_col = max(gals, key=lambda x: x[1])
print(max_row, max_col)

for r in range(max_row[0]):
    if all([r != x[0] for x in gals]):
        empty_rows.append(r)
for c in range(max_col[1]):
    if all([c != x[1] for x in gals]):
        empty_cols.append(c)
new_gal = [x for x in gals]
for x in empty_rows:
    for idx, g in enumerate(gals):
        if x < g[0]:
            new_gal[idx] = (new_gal[idx][0] + 999_999, new_gal[idx][1]) 

for x in empty_cols:
    for idx, g in enumerate(gals):
        if x < g[1]:
            new_gal[idx] = (new_gal[idx][0], new_gal[idx][1] + 999_999) 

def manhattandist(x, y):
    return abs(x[0]-y[0]) + abs(x[1] - y[1])

sum_of_mins = 0
for i, g in enumerate(new_gal):
    dists = list(map(lambda x: manhattandist(g, x) if x != g else 1_000_000_000_000, new_gal))
    #print(dists, min(dists))
    sum_of_mins += sum(dists[i+1:])
print(sum_of_mins)

