with open('puzzle.txt') as f:
    instructions = next(f).strip('\n')
    lines = [line.strip().split(' = ') for line in f if len(line.strip()) != 0]
    nodes = []
    elements = []
    for node, element in lines:
        nodes.append(node)
        elements.append(element.strip(')').strip('(').split(', '))
    start_node = 'AAA'
    l_element, r_element = elements[nodes.index('AAA')]
    found = False
    count = 1
    while True:
        if found is True:
            break
        for i in range(len(instructions)):
            if instructions[i] == 'L':
                if 'ZZZ' in l_element:
                    found = True
                    break
                else:
                    count += 1
                    start_node = l_element
                    l_element, r_element = elements[nodes.index(l_element)]
                    continue
            if instructions[i] == 'R':
                if 'ZZZ' in r_element:
                    found = True
                    break
                else:
                    count += 1
                    start_node = r_element
                    l_element, r_element = elements[nodes.index(r_element)]
                    continue
    print(count)
