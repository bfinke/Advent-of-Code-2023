def start_num(string):
    chars = []
    for char in string:
        try:
            return str(int(char))
        except ValueError:
            chars.append(char)
        for k, v in num_dict.items():
            if k in "".join(chars):
                return v
            else:
                continue


def end_num(string):
    chars = []
    for char in string[::-1]:
        try:
            return str(int(char))
        except ValueError:
            chars.insert(0, char)
        for k, v in num_dict.items():
            if k in "".join(chars):
                return v
            else:
                continue


num_dict = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
            'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
with open('puzzle.txt') as f:
    count = 0
    for line in f:
        count += int(start_num(line) + end_num(line))
print(count)
