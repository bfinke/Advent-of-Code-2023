import math

with open('puzzle.txt') as f:
    time, distance = [line.strip('\n').split(':').pop(1).strip().split() for line in f]
    races = [[int(time[i]), int(distance[i])] for i in range(len(time))]
    record = []
    for t, d in races:
        count = 0
        for m in range(t):
            if (t - m) * m > d:
                count += 1
        record.append(count)
    print(math.prod(record))
