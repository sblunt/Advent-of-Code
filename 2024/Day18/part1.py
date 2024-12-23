"""I get another shot at Dijkstra!"""

import numpy as np

f = open("input.txt", "r")


n_rows = 71
n_cols = 71
n_bits = 1024
maze = np.zeros((n_rows, n_cols), dtype=int)
starting_node = (0, 0)
ending_node = (n_rows - 1, n_cols - 1)

for n_lines, line in enumerate(f.readlines()):
    j = int(line.split(",")[0])
    i = int(line.split(",")[1])

    maze[i, j] = 1

    if n_lines == n_bits - 1:
        break

# initialize unvisited nodes
unvisited_nodes = {}
for i in range(n_rows):
    for j in range(n_cols):
        if not maze[i, j]:
            unvisited_nodes[(i, j)] = np.inf
unvisited_nodes[starting_node] = 0


# logic for choosing current node (again too lazy to do the priority queue, alas...)
def get_current_node(unvisited_nodes):
    min = np.inf
    for key in unvisited_nodes.keys():
        if unvisited_nodes[key] < min:
            current_node = key
            min = unvisited_nodes[key]
    return current_node


# Dijikstra driver
current_node = starting_node
current_score = 0
while current_node != ending_node:

    i, j = current_node

    # update scores of neighbor nodes through current node
    up_node = (i - 1, j)
    if up_node in unvisited_nodes:
        if current_score + 1 < unvisited_nodes[up_node]:
            unvisited_nodes[up_node] = current_score + 1
    down_node = (i + 1, j)
    if down_node in unvisited_nodes:
        if current_score + 1 < unvisited_nodes[down_node]:
            unvisited_nodes[down_node] = current_score + 1
    left_node = (i, j - 1)
    if left_node in unvisited_nodes:
        if current_score + 1 < unvisited_nodes[left_node]:
            unvisited_nodes[left_node] = current_score + 1
    right_node = (i, j + 1)
    if right_node in unvisited_nodes:
        if current_score + 1 < unvisited_nodes[right_node]:
            unvisited_nodes[right_node] = current_score + 1

    # choose new current node, get its score, and remove it from unvisited nodes
    current_node = get_current_node(unvisited_nodes)
    current_score = unvisited_nodes[current_node]
    del unvisited_nodes[current_node]

print(current_score)
