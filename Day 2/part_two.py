with open('puzzle.txt') as f:
    totals = []
    for line in f:
        game, items = line.split(':')
        items = items.split(';')
        blue = 0
        green = 0
        red = 0
        for item in items:
            marbles = item.split(', ')
            for i in marbles:
                if 'blue' in i:
                    i = i.strip()
                    number, color = i.split(' ')
                    if int(number) > blue:
                        blue = int(number)
                if 'green' in i:
                    i = i.strip()
                    number, color = i.split(' ')
                    if int(number) > green:
                        green = int(number)
                if 'red' in i:
                    i = i.strip()
                    number, color = i.split(' ')
                    if int(number) > red:
                        red = int(number)
        totals.append(red * blue * green)
print(sum(totals))