def start_num(string):
    chars = []
    for char in string:
        try:
            char = int(char)
            return str(char)
        except ValueError:
            chars.append(char)
        for k, v in num_dict.items():
            new_string = "".join(chars)
            if k in new_string:
                return v
            else:
                continue


def end_num(string):
    chars = []
    for char in range(len(string) - 1, -1, -1):
        try:
            value = int(string[char])
            return str(value)
        except ValueError:
            chars.insert(0, string[char])
        for k, v in num_dict.items():
            new_string = "".join(chars)
            if k in new_string:
                return v
            else:
                continue


num_dict = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
            'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
with open(input("Enter puzzle: ")) as f:
    count = 0
    for line in f:
        count += int(start_num(line) + end_num(line))
print(count)
