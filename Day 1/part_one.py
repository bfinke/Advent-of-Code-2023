with open('puzzle.txt') as f:
    nums = []
    for line in f:
        num = []
        for i in range(len(line)):
            try:
                start = int(line[i])
                num.append(str(start))
                break
            except ValueError:
                continue
        for i in range(len(line) - 1, -1, -1):
            try:
                end = int(line[i])
                num.append(str(end))
                break
            except ValueError:
                continue
        value = "".join(num)
        nums.append(int(value))
print(sum(nums))
