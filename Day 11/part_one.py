with open('puzzle.txt') as f:
    lines = [line.strip() for line in f]
    new_lines = lines.copy()
    big_rows = []
    for row in lines:
        if row == '.' * len(row):
            big_rows.append(lines.index(row))
            lines[lines.index(row)] = ''
    new_column = len(new_lines)
    new_row = len(new_lines[0])
    lines = []
    for i in range(new_row):
        new_data = []
        for n in range(new_column):
            new_data += new_lines[n][i]
        lines.append(''.join(new_data))
    new_lines = lines.copy()
    big_columns = []
    for row in lines:
        if row == '.' * len(row):
            big_columns.append(lines.index(row))
            lines[lines.index(row)] = ''
    lines = []
    new_column = len(new_lines)
    new_row = len(new_lines[0])
    for i in range(new_row):
        new_data = ''
        for n in range(new_column):
            new_data += new_lines[n][i]
        lines.append(''.join(new_data))
    galaxies = []
    for y, row in enumerate(lines):
        for x, item in enumerate(row):
            if item == '#':
                galaxies.append([x, y])
    used = []
    distances = 0
    for a in galaxies:
        for b in galaxies:
            if [a, b] or [b, a] not in used:
                row_count = 0
                for row in big_rows:
                    if (a[1] < row and b[1] > row) or (b[1] < row and a[1] > row):
                        row_count += 1
                column_count = 0
                for column in big_columns:
                    if (a[0] < column and b[0] > column) or (b[0] < column and a[0] > column):
                        column_count += 1
                distances += abs(b[1] - a[1]) + (1 * row_count)
                distances += abs(b[0] - a[0]) + (1 * column_count)
                used.append([a, b])
    print(distances // 2)
