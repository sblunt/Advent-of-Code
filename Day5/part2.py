import numpy as np

# smells like recursion...


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

with open(
    "/Users/bluez3303/Documents/GitHub/Advent-of-Code/Day5/test_input.txt", "r"
) as f:
    seeds = np.array(f.readline().split(":")[1].split()).astype(int)
    f.readline()
    all_maps = {}
    for _ in range(len(ordered_map_labels)):
        map_label, map = read_next_section(f)

        # sort current map in order of increasing source start number
        map.sort(key=lambda x: x[1])

        all_maps[map_label] = map


def partition_space(min_max, net_change, current_map):
    new_partitions = []
    net_change_array = []

    start_of_partition = min_max[0]
    end_of_partition = min_max[1]
    for line in current_map:
        map_start = line[1]
        map_range = line[2]
        map_end = map_start + map_range - 1
        change_in_map = line[0] - map_start

        if (map_start <= start_of_partition) and (map_end < start_of_partition):
            continue
        if map_start > end_of_partition:
            new_partition = [start_of_partition, end_of_partition]
            new_partitions.append(new_partition)
            net_change_array.append(net_change)
            break
        if (map_start <= start_of_partition) and (map_end < end_of_partition):
            new_partition = [start_of_partition, map_end]
            new_partitions.append(new_partition)
            net_change_array.append(net_change + change_in_map)
            start_of_partition = map_end + 1
        if (map_start <= start_of_partition) and (map_end >= end_of_partition):
            new_partition = [start_of_partition, end_of_partition]
            new_partitions.append(new_partition)
            net_change_array.append(net_change + change_in_map)
            break
        if (map_start > start_of_partition) and (map_end < end_of_partition):
            new_partition1 = [start_of_partition, map_start - 1]
            new_partitions.append(new_partition1)
            net_change_array.append(net_change)
            new_partition2 = [map_start, map_end]
            new_partitions.append(new_partition2)
            net_change_array.append(net_change + change_in_map)
            start_of_partition = map_end + 1
        if (map_start > start_of_partition) and (map_end >= end_of_partition):
            new_partition1 = [start_of_partition, map_start - 1]
            new_partitions.append(new_partition1)
            net_change_array.append(net_change)
            new_partition2 = [map_start, end_of_partition]
            new_partitions.append(new_partition2)
            net_change_array.append(net_change + change_in_map)
            break
    if map_start < start_of_partition:
        new_partitions.append([map_end + 1, end_of_partition])
        net_change_array.append(net_change)

    if map_end < end_of_partition:
        new_partitions.append([map_end + 1, end_of_partition])
        net_change_array.append(net_change)

    return new_partitions, net_change_array


# new_partitions, net_change = partition_space([97, 110], 0, all_maps["seed-to-soil"])
# print(new_partitions)
# print(net_change)


def partition_space_spanned_by_seed_lims(partition_list, net_change_list, map_index):
    if map_index == len(ordered_map_labels):
        return partition_list, net_change_list
    else:
        final_partition_list = []
        final_net_change_list = []
        for i in range(len(partition_list)):
            sub_partition_list, sub_net_change_list = partition_space(
                partition_list[i],
                net_change_list[i],
                all_maps[ordered_map_labels[map_index]],
            )
            final_partition_list.extend(sub_partition_list)
            final_net_change_list.extend(sub_net_change_list)
        return partition_space_spanned_by_seed_lims(
            final_partition_list, final_net_change_list, map_index + 1
        )


all_partitions, all_net_change = partition_space_spanned_by_seed_lims(
    [[82, 83]], [0], 0
)

# finally, iterate through and look for the minimum
min_val = np.inf
for i, min_max in enumerate(all_partitions):
    if all_net_change[i] > 0:
        this_min = min_max[0] + all_net_change[i]
        min_val = np.min([min_val, this_min])
    else:
        this_min = min_max[0] + all_net_change[i]
        min_val = np.min([min_val, this_min])
print(min_val)
