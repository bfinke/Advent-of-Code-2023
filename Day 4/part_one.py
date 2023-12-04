with open('puzzle.txt') as f:
    wins = []
    for line in f:
        card, numbers = line.split(':')
        win_nums, have_nums = numbers.split('|')
        win_nums, have_nums = win_nums.split(' '), have_nums.split(' ')
        winning = [i.strip() for i in win_nums if i != '']
        haves = [i.strip() for i in have_nums if i != '']
        count = 0
        for nums in haves:
            if nums in winning:
                count += 1
        if count != 0:
            wins.append(2 ** (count - 1))
print(sum(wins))
