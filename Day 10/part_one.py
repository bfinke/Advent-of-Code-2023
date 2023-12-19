with open('puzzle.txt') as f:
    lines = [list(line.strip()) for line in f]
    chars = []
    cords = []
    for y, line in enumerate(lines):
        new_line = []
        for x, item in enumerate(line):
            if item == 'S':
                start_cords = [x, y]
            cords.append([x, y])
            new_line.append(item)
        chars.append(new_line)
    cur_char, cur_cords = 'S', start_cords
    count = 1
    dir = ''
    while True:
        if (cur_cords[1] - 1 != -1) and dir != 'ns' and dir != 'nw' and dir != 'ne' and (cur_char == '|' or cur_char == 'L' or cur_char == 'J' or cur_char == 'S'):
            n_char, n_cords = chars[cur_cords[1] - 1][cur_cords[0]], [cur_cords[0], cur_cords[1] - 1]
            if n_char == 'S':
                break
            if n_char == '|':
                cur_char = '|'
                cur_cords = n_cords
                dir = 'sn'
                count += 1
                continue
            if n_char == '7':
                cur_char = '7'
                cur_cords = n_cords
                dir = 'sw'
                count += 1
                continue
            if n_char == 'F':
                cur_char = 'F'
                cur_cords = n_cords
                dir = 'se'
                count += 1
                continue
        if cur_cords[0] + 1 <= len(chars[0]) and dir != 'ew' and dir != 'en' and dir != 'es' and (cur_char == '-' or cur_char == 'L' or cur_char == 'F' or cur_char == 'S'):
            e_char, e_cords = chars[cur_cords[1]][cur_cords[0] + 1], [cur_cords[0] + 1, cur_cords[1]]
            if e_char == 'S':
                break
            if e_char == '-':
                cur_char = '-'
                cur_cords = e_cords
                dir = 'we'
                count += 1
                continue
            if e_char == 'J':
                cur_char = 'J'
                cur_cords = e_cords
                dir = 'wn'
                count += 1
                continue
            if e_char == '7':
                cur_char = '7'
                cur_cords = e_cords
                dir = 'ws'
                count += 1
                continue
        if cur_cords[1] + 1 <= len(chars) and dir != 'se' and dir != 'sw' and dir != 'sn' and (cur_char == '|' or cur_char == 'F' or cur_char == '7' or cur_char == 'S'):
            s_char, s_cords = chars[cur_cords[1] + 1][cur_cords[0]], [cur_cords[0], cur_cords[1] + 1]
            if s_char == 'S':
                break
            if s_char == '|':
                cur_char = '|'
                cur_cords = s_cords
                dir = 'ns'
                count += 1
                continue
            if s_char == 'J':
                cur_char = 'J'
                cur_cords = s_cords
                dir = 'nw'
                count += 1
                continue
            if s_char == 'L':
                cur_char = 'L'
                cur_cords = s_cords
                dir = 'ne'
                count += 1
                continue
        if cur_cords[0] - 1 != -1 and dir != 'we' and dir != 'wn' and dir != 'ws' and (cur_char == '-' or cur_char == 'J' or cur_char == '7' or cur_char == 'S'):
            w_char, w_cords = chars[cur_cords[1]][cur_cords[0] - 1], [cur_cords[0] - 1, cur_cords[1]]
            if w_char == 'S':
                break
            if w_char == '-':
                cur_char = '-'
                cur_cords = w_cords
                dir = 'ew'
                count += 1
                continue
            if w_char == 'L':
                cur_char = 'L'
                cur_cords = w_cords
                dir = 'en'
                count += 1
                continue
            if w_char == 'F':
                cur_char = 'F'
                cur_cords = w_cords
                dir = 'es'
                count += 1
                continue
        if cur_cords == start_cords:
            break
    print(count // 2)
