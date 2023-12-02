with open('puzzle.txt') as f:
    totals = []
    for line in f:
        game, items = line.split(':')
        items = items.split(';')
        blue, green, red = [0, 0, 0]
        for item in items:
            marbles = item.split(',')
            for i in marbles:
                number, color = i.strip().split(' ')
                if color == 'blue' and int(number) > blue:
                    blue = int(number)
                if color == 'green' and int(number) > green:
                    green = int(number)
                if color == 'red' and int(number) > red:
                    red = int(number)
        totals.append(red * blue * green)
print(sum(totals))
