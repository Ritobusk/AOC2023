f = open("in.in").readlines()


rows = len(f)
cols = len(f[0].strip())

total = 0

for i, line in enumerate(f):
    line = line.strip()
    for j, ch in enumerate(line):
        if ch == '*':
            seen_indices = set()
            nums = []
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
                        nums.append(new_num)
            print(nums)
            if len(nums) == 2:
                total += nums[0] * nums[1]
print(total)







