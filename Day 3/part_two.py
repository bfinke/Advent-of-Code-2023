import math


def isNumber(value):
    try:
        value = int(value)
        return True
    except ValueError:
        return False


def getNumber(num_list, num_index_list, start_cords):
    start_index = num_index_list.index(start_cords)
    full_num = []
    count = start_cords[0]
    for x, y in num_index_list[start_index::-1]:
        if x == count and y == start_cords[1]:
            num_start = [x, y]
            continue
        elif x == count - 1 and y == start_cords[1]:
            count -= 1
            num_start = [x, y]
            continue
        else:
            break
    start_index = num_index_list.index(num_start)
    end_index = start_index
    count = num_start[0]
    for x, y in num_index_list[start_index:]:
        if x == count and y == start_cords[1]:
            end_index += 1
            continue
        elif x == count + 1 and y == start_cords[1]:
            count += 1
            end_index += 1
        else:
            break
    cords = []
    count = start_index
    for i in num_list[start_index:end_index]:
        full_num.append(str(i))
        cords.append(num_index_list[count])
        count += 1
    return int("".join(full_num)), cords


with open("puzzle.txt") as f:
    file = f.readlines()
    lines = [line.strip('\n') for line in file]

symbol_index = []
num, num_index = [], []
for y, line in enumerate(lines):
    for x, item in enumerate(line):
        if isNumber(item) is True:
            num.append(int(item))
            num_index.append([x, y])
        if item == '*':
            symbol_index.append([x, y])
        if item == '.':
            continue
included_numbers = []
included_cords = []
for x_sym, y_sym in symbol_index:
    num_gear = []
    for x_num, y_num in num_index:
        # Symbol to the left of number
        if (x_sym == x_num - 1) and (y_sym == y_num):
            number, cords = getNumber(num, num_index, [x_num, y_num])
            if cords[0] not in included_cords:
                num_gear.append(number)
                for cord in cords:
                    included_cords.append(cord)
        # Symbol to the right of number
        if (x_sym == x_num + 1) and (y_sym == y_num):
            number, cords = getNumber(num, num_index, [x_num, y_num])
            if cords[0] not in included_cords:
                num_gear.append(number)
                for cord in cords:
                    included_cords.append(cord)
        # Symbol straight above number
        if (x_sym == x_num) and (y_sym == y_num + 1):
            number, cords = getNumber(num, num_index, [x_num, y_num])
            if cords[0] not in included_cords:
                num_gear.append(number)
                for cord in cords:
                    included_cords.append(cord)
        # Symbol straight below number
        if (x_sym == x_num) and (y_sym == y_num - 1):
            number, cords = getNumber(num, num_index, [x_num, y_num])
            if cords[0] not in included_cords:
                num_gear.append(number)
                for cord in cords:
                    included_cords.append(cord)
        # Symbol is up and to the left
        if (x_sym == x_num - 1) and (y_sym == y_num + 1):
            number, cords = getNumber(num, num_index, [x_num, y_num])
            if cords[0] not in included_cords:
                num_gear.append(number)
                for cord in cords:
                    included_cords.append(cord)
        # Symbol is up and to the right
        if (x_sym == x_num + 1) and (y_sym == y_num + 1):
            number, cords = getNumber(num, num_index, [x_num, y_num])
            if cords[0] not in included_cords:
                num_gear.append(number)
                for cord in cords:
                    included_cords.append(cord)
        # Symbol is down and to the left
        if (x_sym == x_num - 1) and (y_sym == y_num - 1):
            number, cords = getNumber(num, num_index, [x_num, y_num])
            if cords[0] not in included_cords:
                num_gear.append(number)
                for cord in cords:
                    included_cords.append(cord)
        # Symbol is down and to the right
        if (x_sym == x_num + 1) and (y_sym == y_num - 1):
            number, cords = getNumber(num, num_index, [x_num, y_num])
            if cords[0] not in included_cords:
                num_gear.append(number)
                for cord in cords:
                    included_cords.append(cord)
    if len(num_gear) == 2:
        included_numbers.append(math.prod(num_gear))
print(sum(included_numbers))
