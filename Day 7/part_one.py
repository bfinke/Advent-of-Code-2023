with open('puzzle.txt') as f:
    data = [line.strip().split(' ') for line in f.readlines()]
five_kinds = []
four_kinds = []
full_houses = []
three_kinds = []
two_pairs = []
one_pairs = []
high_cards = []
for hand, bid in data:
    card_dict = {'A': 0, 'K': 0, 'Q': 0, 'J': 0, 'T': 0, '9': 0,
                 '8': 0, '7': 0, '6': 0, '5': 0, '4': 0, '3': 0, '2': 0}
    for char in hand:
        card_dict[char] += 1
    values = []
    for v in card_dict.values():
        values.append(v)
    max_value = max(values)
    if max_value == 5:
        five_kinds.append([hand, bid])
    elif max_value == 4:
        four_kinds.append([hand, bid])
    elif max_value == 3:
        if 2 in values:
            full_houses.append([hand, bid])
        else:
            three_kinds.append([hand, bid])
    elif max_value == 2:
        count = 0
        while True:
            if max_value in values:
                count += 1
                del values[values.index(max_value)]
            else:
                break
        if count == 2:
            two_pairs.append([hand, bid])
        else:
            one_pairs.append([hand, bid])
    else:
        high_cards.append([hand, bid])
sorts = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
five_kinds = sorted(five_kinds, key=lambda x: [sorts.index(char) for char in x[0]])
four_kinds = sorted(four_kinds, key=lambda x: [sorts.index(char) for char in x[0]])
full_houses = sorted(full_houses, key=lambda x: [sorts.index(char) for char in x[0]])
three_kinds = sorted(three_kinds, key=lambda x: [sorts.index(char) for char in x[0]])
two_pairs = sorted(two_pairs, key=lambda x: [sorts.index(char) for char in x[0]])
one_pairs = sorted(one_pairs, key=lambda x: [sorts.index(char) for char in x[0]])
high_cards = sorted(high_cards, key=lambda x: [sorts.index(char) for char in x[0]])
all_hands = []
[all_hands.append(item) for item in five_kinds]
[all_hands.append(item) for item in four_kinds]
[all_hands.append(item) for item in full_houses]
[all_hands.append(item) for item in three_kinds]
[all_hands.append(item) for item in two_pairs]
[all_hands.append(item) for item in one_pairs]
[all_hands.append(item) for item in high_cards]
rank = len(all_hands)
total = 0
for hand, bid in all_hands:
    total += int(bid) * rank
    rank -= 1
print(total)
