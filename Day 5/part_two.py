def seed_finder(end, destination_category):
    for test in destination_category:
        destination_start, source_start, size_range = test.split(' ')
        if end <= int(destination_start) + int(size_range) - 1 and end >= int(destination_start):
            return end - int(destination_start) + int(source_start)
    return end


map_types = {}
with open('puzzle.txt') as f:
    file = f.readlines()
    lines = [line.strip('\n') for line in file if len(line.strip()) > 0]
    maps = []
    value_indexes = []
    for items in lines:
        if lines.index(items) == 0:
            seeds = items.split(' ')
            seeds = seeds[1:]
            continue
        try:
            destination, source, size = items.split()
            value_indexes.append(lines.index(items))
        except ValueError:
            maps.append(items)
new_range = []
count = 0
for s in range(len(seeds) // 2):
    new_range.append([int(seeds[s + count]), int(seeds[s + count]) + int(seeds[s + count + 1]) - 1])
    count += 1
indexes = []
ranges = []
for i in value_indexes:
    if len(indexes) == 0:
        indexes.append(i)
    elif i - 1 == indexes[-1]:
        indexes.append(i)
    else:
        indexes[-1] += 1
        ranges.append([indexes[0], indexes[-1]])
        indexes = []
        indexes.append(i)
indexes[-1] += 1
ranges.append([indexes[0], indexes[-1]])
indexes = []
indexes.append(i)
for c in range(len(maps)):
    map_types[maps[c]] = lines[ranges[c][0]:ranges[c][1]]
maps = []
map_values = []
for k, v in map_types.items():
    maps.insert(0, k)
    map_values.insert(0, v)
location = 0
found_location = False
while True:
    seed_value = location
    if found_location is True:
        break
    for i in range(len(maps)):
        seed_value = seed_finder(seed_value, map_values[i])
    for start_value, end_value in new_range:
        if seed_value >= start_value and seed_value <= end_value:
            found_location = True
            break
    location += 1
print(location - 1)
