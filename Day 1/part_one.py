with open('puzzle.txt') as f:
    nums = []
    for line in f:
        num = []
        for i in line:
            try:
                num.append(str(int(i)))
                break
            except ValueError:
                continue
        for i in line[::-1]:
            try:
                num.append(str(int(i)))
                break
            except ValueError:
                continue
        nums.append(int("".join(num)))
print(sum(nums))
