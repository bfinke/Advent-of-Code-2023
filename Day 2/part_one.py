with open('puzzle.txt') as f:
    game_possible = []
    for line in f:
        game, items = line.split(':')
        game = int(game.replace('Game ', ''))
        game_possible.append(game)
        items = items.split(';')
        for item in items:
            if game not in game_possible:
                break
            marbles = item.split(',')
            for i in marbles:
                number, color = i.strip().split(' ')
                if color == 'blue' and int(number) > 14:
                    game_possible.remove(game)
                    break
                if color == 'green' and int(number) > 13:
                    game_possible.remove(game)
                    break
                if color == 'red' and int(number) > 12:
                    game_possible.remove(game)
                    break
print(sum(game_possible))
