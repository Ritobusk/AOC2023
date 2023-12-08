f = open("test3.in").readlines()

instructions = f[0].strip()

nodes = {}
for line in f[2:]:
    name, rest = line.split(" = ")
    rest = rest.strip().split(", ")
    left = rest[0][1:len(rest[0])]
    right = rest[1][:len(rest[1]) - 1]
    nodes[name] = [left, right]

cond = True
curr_nodes_keys = list(filter(lambda x: x[-1] == 'A', nodes.keys()))
curr_nodes = []
for x in curr_nodes_keys:
    curr_nodes.append(nodes[x])
ghost_node_count = len(curr_nodes)
print(curr_nodes_keys, ghost_node_count)
steps = 0
while cond:
    for instruction in instructions:
        next_nodes = []
        if instruction == 'L':
            for c_n in curr_nodes: 
                next_nodes.append(nodes[c_n[0]])

        else:
            for c_n in curr_nodes: 
                next_nodes.append(nodes[c_n[1]])
        steps += 1
        end_ghost_nodes = [x for x in next_nodes if x.name[-1] == 'Z']
        #if len(end_ghost_nodes) > 1:
            #print([x.name for x in next_nodes], [x.name for x in end_ghost_nodes], steps)
        if steps % 1000000 == 0:
            print(steps)

        #print(curr_node.name, instruction, next_node.name)
        if  ghost_node_count == len(end_ghost_nodes):
            cond = False
            break
        else:
            curr_nodes = next_nodes

print(steps)



            
