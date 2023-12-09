from math import lcm


with open('puzzle.txt') as f:
    instructions = next(f).strip('\n')
    lines = [line.strip().split(' = ') for line in f if len(line.strip()) != 0]
    nodes = []
    elements = []
    for node, element in lines:
        nodes.append(node)
        elements.append(element.strip(')').strip('(').split(', '))
    network_dict = {}
    for n in nodes:
        if n[-1] == 'A':
            network_dict[n] = elements[nodes.index(n)]
    counts = []
    for node, element in network_dict.items():
        found = False
        count = 0
        l_element, r_element = element
        while True:
            if found is True:
                break
            for i in range(len(instructions)):
                if instructions[i] == 'L':
                    if node[-1] == 'Z':
                        found = True
                        counts.append(count)
                        break
                    else:
                        count += 1
                        node = l_element
                        l_element, r_element = elements[nodes.index(l_element)]
                        continue
                if instructions[i] == 'R':
                    if node[-1] == 'Z':
                        found = True
                        counts.append(count)
                        break
                    else:
                        count += 1
                        node = r_element
                        l_element, r_element = elements[nodes.index(r_element)]
                        continue
    print(lcm(*counts))
