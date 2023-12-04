def total_wins(init_card, card_wins, dict):
    wins = 1
    if card_wins == 0:
        return 1
    card = init_card
    for i in range(1, card_wins + 1):
        wins += total_wins(card + i, dict[card + i], dict)
    return wins


card_dict = {}
with open('puzzle.txt') as f:
    file = f.readlines()
    lines = [i.strip('\n') for i in file]
    for line in lines:
        card, numbers = line.split(':')
        card = card.split(' ')
        win_nums, have_nums = numbers.split('|')
        win_nums, have_nums = win_nums.split(' '), have_nums.split(' ')
        winning = [i.strip() for i in win_nums if i != '']
        haves = [i.strip() for i in have_nums if i != '']
        count = 0
        for nums in haves:
            if nums in winning:
                count += 1
        card_dict[int(card[-1])] = count
totals = []
for k, v in card_dict.items():
    totals.append(total_wins(k, v, card_dict))
print(sum(totals))
