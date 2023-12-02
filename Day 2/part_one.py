with open('puzzle.txt') as f:
    game_possible = []
    for line in f:
        game, items = line.split(':')
        game_possible.append(game)
        items = items.split(';')
        for item in items:
            if game not in game_possible:
                break
            marbles = item.split(', ')
            for i in marbles:
                if 'blue' in i:
                    i = i.strip()
                    number, color = i.split(' ')
                    if int(number) > 14:
                        game_possible.remove(game)
                        break
                if 'green' in i:
                    i = i.strip()
                    number, color = i.split(' ')
                    if int(number) > 13:
                        game_possible.remove(game)
                        break
                if 'red' in i:
                    i = i.strip()
                    number, color = i.split(' ')
                    if int(number) > 12:
                        game_possible.remove(game)
                        break
count = 0
for ids in game_possible:
    game, id = ids.split(' ')
    count += int(id)
print(count)
