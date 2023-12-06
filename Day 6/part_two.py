with open('puzzle.txt') as f:
    time, distance = [line.strip('\n').split(':').pop(1).strip().split() for line in f]
    time, distance = [int(''.join(time)), int(''.join(distance))]
    count = 0
    for m in range(time):
        if (time - m) * m > distance:
            count += 1
    print(count)
