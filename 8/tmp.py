f = open("in.in").readlines()

instructions = f[0].strip()

nodes = {}
for line in f[2:]:
    name, rest = line.split(" = ")
    rest = rest.strip().split(", ")
    left = rest[0][1:len(rest[0])]
    right = rest[1][:len(rest[1]) - 1]
    nodes[name] = [left, right]

curr_nodes_keys = list(filter(lambda x: x[-1] == 'A', nodes.keys()))
curr_nodes = []
for x in curr_nodes_keys:
    curr_nodes.append(x)
steps_in_cycle = [0 for x in curr_nodes]
print(curr_nodes_keys)
for cn_idx, node in enumerate(curr_nodes): 
    steps = 0
    cond = True
    z_nodes = []
    #print(node, nodes)
    tmp_node = nodes[node]
    while cond:
        for instruction in instructions:
            steps += 1
            if instruction == 'L':
                if tmp_node[0][-1] == "Z":
                    z_nodes.append(tmp_node[0])
                    if next_node[0] in z_nodes:
                        #print("HEY", z_nodes)
                        cond = False
                        steps_in_cycle[cn_idx] = steps 
                        break
                next_node = nodes[tmp_node[0]]
            else:
                if next_node[1][-1] == "Z":
                    z_nodes.append(tmp_node[1])
                    if next_node[1] in z_nodes:
                        #print("HEY", z_nodes)
                        cond = False
                        steps_in_cycle[cn_idx] = steps 
                        break
                next_node = nodes[tmp_node[1]]
                
                

            tmp_node = next_node
import math


def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)


res = steps_in_cycle[0]

for i in range(1, len(steps_in_cycle)):
    res = lcm(res, steps_in_cycle[i])

print(steps, steps_in_cycle)
print(res)
