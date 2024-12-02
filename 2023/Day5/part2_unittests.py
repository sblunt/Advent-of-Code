import numpy as np

from part2 import (
    _partition_space_single_map_rule,
    _partition_space_single_map,
    all_maps,
)


def unit_test(
    map_start=50,
    map_end=100,
    change_in_map=10,
    current_partition_starts=[0],
    end_of_partition=49,
    net_change=[0],
    expected_partitions=[0],
    expected_net_changes=[0],
):
    new_partitions, end_of_partition, net_change, _ = _partition_space_single_map_rule(
        current_partition_starts,
        end_of_partition,
        net_change,
        map_start,
        map_end,
        change_in_map,
    )
    assert np.all(new_partitions == expected_partitions)
    assert np.all(expected_net_changes == net_change)


# # case 3
# unit_test(map_start=0, map_end=100, expected_partitions=[0], expected_net_changes=[10])


# # case 1
# unit_test()

# unit_test(
#     end_of_partition=50, expected_partitions=[0, 50], expected_net_changes=[0, 10]
# )
# unit_test(
#     current_partition_starts=[50],
#     end_of_partition=50,
#     expected_partitions=[50],
#     expected_net_changes=[10],
# )

# # case 2
# unit_test(map_start=-2, map_end=-1, expected_partitions=[0], expected_net_changes=[0])


# # case 3
# unit_test(map_start=-2, map_end=110, expected_partitions=[0], expected_net_changes=[10])
# unit_test(map_start=0, map_end=110, expected_partitions=[0], expected_net_changes=[10])

# # case 4
# unit_test(
#     map_start=-2, map_end=0, expected_partitions=[0, 1], expected_net_changes=[10, 0]
# )
# unit_test(
#     map_start=0,
#     map_end=20,
#     expected_partitions=[0, 21],
#     expected_net_changes=[10, 0],
# )

# # case 5
# unit_test(
#     map_start=1,
#     map_end=20,
#     expected_partitions=[0, 1, 21],
#     expected_net_changes=[0, 10, 0],
# )

# # case 6
# unit_test(
#     map_start=1,
#     map_end=100,
#     expected_partitions=[0, 1],
#     expected_net_changes=[0, 10],
# )


# new_partitions, end_of_partition, net_change = _partition_space_single_map(
#     [98], 98, [0], [all_maps["seed-to-soil"][0]]
# )
# assert np.all(new_partitions == [98])
# assert np.all(net_change == [-48])

# new_partitions, end_of_partition, net_change = _partition_space_single_map(
#     [98], 98, [0], [all_maps["seed-to-soil"][1]]
# )
# assert np.all(new_partitions == [98])
# assert np.all(net_change == [0])

new_partitions, end_of_partition, net_change = _partition_space_single_map(
    [98], 98, [0], all_maps["seed-to-soil"]
)
print(new_partitions)
print(net_change)
assert np.all(new_partitions == [98])
assert np.all(net_change == [-48])
