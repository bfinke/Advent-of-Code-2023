def destination_finder(current_source, destination_category):
    for test in destination_category:
        destination_start, source_start, size_range = test.split(' ')
        if current_source >= int(source_start) and current_source <= int(source_start) + int(size_range) - 1:
            return int(destination_start) + current_source - int(source_start)
    return current_source


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
locations = []
for seed in seeds:
    destination = []
    source = seed
    for v in map_types.values():
        source = destination_finder(int(source), v)
        destination.append(source)
    locations.append(destination[-1])
print(min(locations))
