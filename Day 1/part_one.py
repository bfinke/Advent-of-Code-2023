with open('puzzle.txt') as f:
    nums = []
    for line in f:
        num = []
        for i in line:
            try:
                start = int(i)
                num.append(str(start))
                break
            except ValueError:
                continue
        for i in line[::-1]:
            try:
                end = int(i)
                num.append(str(end))
                break
            except ValueError:
                continue
        value = "".join(num)
        nums.append(int(value))
print(sum(nums))