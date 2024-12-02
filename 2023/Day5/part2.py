import numpy as np
from copy import deepcopy

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
    # "soil-to-fertilizer",
    # "fertilizer-to-water",
    # "water-to-light",
    # "light-to-temperature",
    # "temperature-to-humidity",
    # "humidity-to-location",
]

with open(
    "/Users/bluez3303/Documents/GitHub/Advent-of-Code/Day5/test_input.txt", "r"
) as f:
    seeds = np.array(f.readline().split(":")[1].split()).astype(int)
    f.readline()
    all_maps = {}
    for _ in range(len(ordered_map_labels)):
        map_label, map = read_next_section(f)
        all_maps[map_label] = map

        # # sort current map in order of increasing source start number
        # map.sort(key=lambda x: x[1])


# iterate through all current partitions, and split them into smaller partitions
# based on map rules. For the first map rule, partition the entire space. For the next map rule,
# partition the new space given the output of the last.


def _partition_space_single_map_rule(
    partition_starts_list,
    end_of_whole_partition,
    net_change_list,
    map_start,
    map_end,
    change_in_map,
):
    partition_starts_to_return = []
    net_change_to_return = []
    net_change_for_next_map_rule = []
    for i, start_of_partition in enumerate(partition_starts_list):
        map_start = map_start - net_change_list[i]
        map_end = map_end - net_change_list[i]
        # define start and end of sub-partition
        if i == len(partition_starts_list) - 1:
            end_of_partition = end_of_whole_partition
        else:
            end_of_partition = partition_starts_list[i + 1] - 1

        # add current start of partition to final list to return
        partition_starts_to_return.append(start_of_partition)
        net_change_to_return.append(net_change_list[i])
        net_change_for_next_map_rule.append(net_change_list[i])

        # figure out if the map rule needs to be applied
        if map_start <= end_of_partition:
            # case 2
            if map_end < start_of_partition:
                continue

            # case 3
            elif (map_start <= start_of_partition) and (map_end > end_of_partition):
                net_change_to_return[i] += change_in_map
                continue

            # case 4
            elif (map_start <= start_of_partition) and (map_end <= end_of_partition):
                partition_starts_to_return.append(map_end + 1)
                net_change_to_return[i] += change_in_map
                net_change_to_return.append(net_change_list[i])
                net_change_for_next_map_rule.append(net_change_list[i])

            # case 5
            elif (map_start > start_of_partition) and (map_end < end_of_partition):
                partition_starts_to_return.append(map_start)
                partition_starts_to_return.append(map_end + 1)
                net_change_to_return.append(net_change_list[i] + change_in_map)
                net_change_to_return.append(net_change_list[i])
                net_change_for_next_map_rule.append(net_change_list[i])
                net_change_for_next_map_rule.append(net_change_list[i])

            # case 6
            elif (map_start >= start_of_partition) and (map_end > end_of_partition):
                partition_starts_to_return.append(map_start)
                net_change_to_return.append(net_change_list[i] + change_in_map)
                net_change_for_next_map_rule.append(net_change_list[i])

    return (
        partition_starts_to_return,
        end_of_partition,
        net_change_to_return,
        net_change_for_next_map_rule,
    )


def _partition_space_single_map(
    partition_starts_list, end_of_partition, net_change_list, current_map
):
    net_change_for_next_map_rule = deepcopy(net_change_list)
    for line in current_map:
        map_start = line[1]
        map_range = line[2]
        map_end = map_start + map_range - 1
        change_in_map = line[0] - line[1]

        (
            partition_starts_list,
            end_of_partition,
            net_change_list,
            net_change_for_next_map_rule,
        ) = _partition_space_single_map_rule(
            partition_starts_list,
            end_of_partition,
            net_change_for_next_map_rule,
            map_start,
            map_end,
            change_in_map,
        )

    return partition_starts_list, end_of_partition, net_change_list


def partition_space_spanned_by_seed_lims(
    partition_starts, partition_end, net_change_list, map_index
):
    if map_index == len(ordered_map_labels):
        return partition_starts, partition_end, net_change_list
    else:
        (
            final_partition_list,
            partition_end,
            final_net_change_list,
        ) = _partition_space_single_map(
            partition_starts,
            partition_end,
            net_change_list,
            all_maps[ordered_map_labels[map_index]],
        )

        return partition_space_spanned_by_seed_lims(
            final_partition_list, partition_end, final_net_change_list, map_index + 1
        )


# all_partitions, _, all_net_change = partition_space_spanned_by_seed_lims(
#     [80], 83, [0], 0
# )
# print(all_partitions)
# print(all_net_change)
# print(np.min(np.array(all_partitions) + np.array(all_net_change)))

""""





"""

# # sort current map in order of increasing source start number
# map.sort(key=lambda x: x[1])

# def partition_space(partition_list, net_change_list, current_map):
#     start_of_partition = partition_list[0]
#     net_change_so_far = net_change_list[0]

#     # remove end of partititon from list
#     end_of_partition = partition_list.pop()

#     for line in current_map:
#         map_start = line[1] - net_change_so_far
#         map_range = line[2] - net_change_so_far
#         map_end = map_start + map_range - 1 - net_change_so_far
#         change_in_map = line[0] - line[1]

#         # case 1
#         if map_start > end_of_partition:
#             break

#         if map_start <= end_of_partition:
#             # case 2
#             if map_end < start_of_partition:
#                 continue

#             # case 3
#             elif map_end >= end_of_partition:
#                 net_change_list[-1] += change_in_map
#                 break

#             # if we make it here, the end of the map must be between the
#             # beginning & end of the current partition
#             else:
#                 # case 4
#                 if map_start <= start_of_partition:
#                     partition_list.append(map_end + 1)
#                     net_change_list[-1] += change_in_map
#                     net_change_list.append(net_change_so_far)

#                     # increment index
#                     start_of_partition = map_end + 1
#                 # case 5
#                 else:
#                     partition_list.append(map_start)
#                     partition_list.append(map_end + 1)
#                     net_change_list.append(net_change_so_far + change_in_map)
#                     net_change_list.append(net_change_so_far)

#                     # increment index
#                     start_of_partition = map_end + 1

#     # put end of partition back on list
#     partition_list.append(end_of_partition)
#     return partition_list, net_change_list


# new_partitions, net_change = partition_space([0, 97], [2], all_maps["seed-to-soil"])
# print(new_partitions)
# print(net_change)


# # all_partitions, all_net_change = partition_space_spanned_by_seed_lims([82, 83], [0], 0)
# # print(all_partitions)
# # print(all_net_change)
# # print(all_partitions[0] - all_net_change[0])

# # # finally, iterate through and look for the minimum
# # min_val = np.inf
# # for i, min_max in enumerate(all_partitions):
# #     if all_net_change[i] > 0:
# #         this_min = min_max[0] + all_net_change[i]
# #         min_val = np.min([min_val, this_min])
# #     else:
# #         this_min = min_max[0] + all_net_change[i]
# #         min_val = np.min([min_val, this_min])
# # print(min_val)
