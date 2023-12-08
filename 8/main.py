f = open("test3.in").readlines()

instructions = f[0].strip()

class node:
    def __init__(self, left, right, name):
        self.left = left
        self.right = right
        self.name = name

    def PrintName(self):
        print(self.data)

nodes = {}
for line in f[2:]:
    name, rest = line.split(" = ")
    rest = rest.strip().split(", ")
    left = rest[0][1:len(rest[0])]
    right = rest[1][:len(rest[1]) - 1]
    nodes[name] = node(left, right, name)
cond = True
ending_with_A = list(filter(lambda x: x[-1] == 'A', nodes.keys()))
print(ending_with_A)
print(curr_node.name)
curr_node = nodes[0]
steps = 0
while cond:
    for instruction in instructions:
        next_nodes = []
        if instruction == 'L':
            next_node = nodes[curr_node.left]
        else:
            next_node = nodes[curr_node.right]
        steps += 1
        #print(curr_node.name, instruction, next_node.name)
        if next_node.name == "ZZZ":
            cond = False
            break
        else:
            curr_node = next_node

print(steps)



            
