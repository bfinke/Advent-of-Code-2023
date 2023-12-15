with open('puzzle.txt') as f:
    lines = [[int(i) for i in line.split()] for line in f]
    total = 0
    for nums in lines:
        diffs = [nums]
        while True:
            if diffs[-1].count(0) == len(diffs[-1]):
                break
            new_nums = []
            for i in range(len(diffs[-1]) - 1):
                new_nums.append(diffs[-1][i + 1] - diffs[-1][i])
            diffs.append(new_nums)
        diffs[-1].insert(0, 0)
        for i in range(len(diffs) - 1):
            diffs[len(diffs) - i - 2].insert(0, diffs[len(diffs) - i - 2][0] - diffs[len(diffs) - i - 1][0])
        total += diffs[0][0]
    print(total)
