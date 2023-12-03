f = open("in.in").readlines()

seen_indices = set()

rows = len(f)
cols = len(f[0].strip())

total = 0

for i, line in enumerate(f):
    line = line.strip()
    for j, ch in enumerate(line):
        if ch != '.' and not ch.isdigit():
            for r, c in [(i-1,j),(i-1,j-1),(i-1,j+1),(i,j+1),(i,j-1),(i+1, j-1),(i+1,j),(i+1,j+1)]:
                if rows > r >= 0 and cols > c >= 0:
                    if f[r][c].isdigit() and (r,c) not in seen_indices:
                        seen_indices.add((r,c))
                        go_left = True
                        go_right = True
                        
                        num = [int(f[r][c])]
                        offset = 1
                        while go_left or go_right:
                            if f[r][c + offset].isdigit() and go_right and c + offset < cols:
                                seen_indices.add((r, c + offset))
                                num.append(int(f[r][c+offset]))
                            else:
                                go_right = False
                            if f[r][c - offset].isdigit() and go_left and c - offset >= 0:
                                seen_indices.add((r, c - offset))
                                num.insert(0, int(f[r][c-offset]))
                            else:
                                go_left = False
                            offset += 1
                        new_num = 0
                        print("new num:", num)
                        for n in range(len(num)):
                            new_num += num[n] * (pow(10,len(num) - n - 1))
                        total += new_num
print(total)







