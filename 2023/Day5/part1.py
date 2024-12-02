import numpy as np


def read_next_section(f):
    map_label = f.readline()[:-6]
    map = []
    while True:
        map_entry = f.readline().split()
        if not map_entry:
            break
        map.append(np.array(map_entry).astype(int))

    return map_label, map


ordered_map_labels = [
    "seed-to-soil",
    "soil-to-fertilizer",
    "fertilizer-to-water",
    "water-to-light",
    "light-to-temperature",
    "temperature-to-humidity",
    "humidity-to-location",
]

with open("input.txt", "r") as f:
    seeds = np.array(f.readline().split(":")[1].split()).astype(int)
    f.readline()
    all_maps = {}
    for _ in range(len(ordered_map_labels)):
        map_label, map = read_next_section(f)
        all_maps[map_label] = map


def seed_to_location(seed_num):
    """
    Args:
        seed_num (int)

    Returns:
        int: location
    """
    source_index = seed_num
    for map_label in ordered_map_labels:
        current_map = all_maps[map_label]
        for line in current_map:
            source_min = line[1]
            range = line[2]
            source_max = source_min + range - 1
            if (source_index >= source_min) and (source_index <= source_max):
                # source index is in range; get dest index and update
                source_index = line[0] + (source_index - source_min)
                break
            else:
                pass  # source index stays the same if it doesn't match anything in the map

    return source_index


location_numbers = []
for seed in seeds:
    location_numbers.append(seed_to_location(seed))

print("Minimum location number: {}".format(np.min(location_numbers)))
