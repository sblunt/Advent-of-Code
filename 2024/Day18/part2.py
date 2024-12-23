"""

Idea: just find all nodes touching starting node, and check if end node is in it

(This is quite slow but it works eventually. Set and forget just like my MCMCs lol.)

"""

import numpy as np
import sys


sys.setrecursionlimit(100_000)


def find_all_nodes_touching_current(node, maze, all_nodes):
    i, j = node

    # check up
    up_node = (i - 1, j)
    up_nodes = set()
    if i > 0:
        if not maze[up_node] and up_node not in all_nodes:
            all_nodes.add(up_node)
            up_nodes = find_all_nodes_touching_current(up_node, maze, all_nodes)

    # check down
    down_node = (i + 1, j)
    down_nodes = set()
    if i < n_rows - 1:
        if not maze[down_node] and down_node not in all_nodes:
            all_nodes.add(down_node)
            down_nodes = find_all_nodes_touching_current(down_node, maze, all_nodes)

    # check right
    right_node = (i, j + 1)
    right_nodes = set()
    if j < n_cols - 1:
        if not maze[right_node] and right_node not in all_nodes:
            all_nodes.add(right_node)
            right_nodes = find_all_nodes_touching_current(right_node, maze, all_nodes)

    # check left
    left_node = (i, j - 1)
    left_nodes = set()
    if j > 0:
        if not maze[left_node] and left_node not in all_nodes:
            all_nodes.add(left_node)
            left_nodes = find_all_nodes_touching_current(left_node, maze, all_nodes)
    return all_nodes | right_nodes | left_nodes | up_nodes | down_nodes


n_rows = 71
n_cols = 71
maze = np.zeros((n_rows, n_cols), dtype=int)
starting_node = (0, 0)
ending_node = (n_rows - 1, n_cols - 1)


f = open("input.txt", "r")
for n_lines, line in enumerate(f.readlines()):
    print(n_lines, end="\r")
    j = int(line.split(",")[0])
    i = int(line.split(",")[1])

    maze[i, j] = 1

    all_nodes = find_all_nodes_touching_current(starting_node, maze, set())
    if ending_node not in all_nodes:
        print(f"{j},{i}")
        break
