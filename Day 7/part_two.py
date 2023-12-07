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
    card_dict = {'A': 0, 'K': 0, 'Q': 0, 'T': 0, '9': 0, '8': 0,
                 '7': 0, '6': 0, '5': 0, '4': 0, '3': 0, '2': 0, 'J': 0}
    for char in hand:
        card_dict[char] += 1
    values = []
    j_count = card_dict['J']
    card_dict['J'] = 0
    for v in card_dict.values():
        values.append(v)
    max_value = max(values)
    ones = values.count(1)
    twos = values.count(2)
    threes = values.count(3)
    if ((j_count >= 4) or (j_count == 3 and max_value == 2) or (j_count == 2 and max_value == 3) or
        (j_count == 1 and max_value == 4) or (max_value == 5)):
        five_kinds.append([hand, bid])
    elif ((j_count == 3 and max_value == 1) or (j_count == 2 and max_value == 2) or
          (j_count == 1 and max_value == 3) or (max_value == 4)):
        four_kinds.append([hand, bid])
    elif (j_count == 2 and max_value == 1) or (j_count == 1 and max_value == 2) or (max_value == 3):
        if (j_count == 1 and twos == 2) or (twos == 1 and threes == 1):
            full_houses.append([hand, bid])
        else:
            three_kinds.append([hand, bid])
    elif (twos == 2 and ones == 1):
        two_pairs.append([hand, bid])
    elif (twos == 1 and ones == 3) or (j_count == 1 and ones == 4):
        one_pairs.append([hand, bid])
    else:
        high_cards.append([hand, bid])
sorts = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
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
