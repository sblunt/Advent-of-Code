import numpy as np

"""
First: go through dijkstra & assign every tile a minimum score
"""


f = open(
    "input.txt",
    "r",
)

maze = []

for line in f.readlines():
    line_list = []
    for i in line:
        if i != "\n":
            line_list.append(i)
    maze.append(line_list)

maze = np.array(maze)

n_rows = len(maze)
n_cols = len(maze[0])


def get_next_current_node(unvisited_nodes):
    min = np.inf
    for key in unvisited_nodes.keys():
        if unvisited_nodes[key] < min:
            min = unvisited_nodes[key]
            current_node = key
    return current_node


unvisited_nodes = {}
visited_nodes = {}
for i in range(n_rows):
    for j in range(n_cols):
        if maze[i, j] == ".":
            unvisited_nodes[(i, j, "left")] = np.inf
            unvisited_nodes[(i, j, "up")] = np.inf
            unvisited_nodes[(i, j, "down")] = np.inf
            unvisited_nodes[(i, j, "right")] = np.inf
        if maze[i, j] == "E":
            unvisited_nodes[(i, j, "right")] = np.inf
            unvisited_nodes[(i, j, "up")] = np.inf
            ending_node_right = (i, j, "right")
            ending_node_up = (i, j, "up")
        elif maze[i, j] == "S":
            current_node = (i, j, "right")
            unvisited_nodes[current_node] = 0
            unvisited_nodes[(i, j, "left")] = np.inf
            unvisited_nodes[(i, j, "up")] = np.inf
            unvisited_nodes[(i, j, "down")] = np.inf
            starting_node = current_node

while ending_node_right in unvisited_nodes or ending_node_up in unvisited_nodes:

    i, j, current_direction = current_node

    current_score = unvisited_nodes[current_node]
    del unvisited_nodes[current_node]

    """
    update neighbor node scores
    """

    if current_direction == "right":
        if (i, j + 1, "right") in unvisited_nodes:
            score_through_current_node = current_score + 1
            if score_through_current_node < unvisited_nodes[(i, j + 1, "right")]:
                unvisited_nodes[(i, j + 1, "right")] = score_through_current_node
        if (i, j, "up") in unvisited_nodes:
            score_through_current_node = current_score + 1000
            if score_through_current_node < unvisited_nodes[(i, j, "up")]:
                unvisited_nodes[(i, j, "up")] = score_through_current_node
        if (i, j, "down") in unvisited_nodes:
            score_through_current_node = current_score + 1000
            if score_through_current_node < unvisited_nodes[(i, j, "down")]:
                unvisited_nodes[(i, j, "down")] = score_through_current_node
    if current_direction == "left":
        if (i, j - 1, "left") in unvisited_nodes:
            score_through_current_node = current_score + 1
            if score_through_current_node < unvisited_nodes[(i, j - 1, "left")]:
                unvisited_nodes[(i, j - 1, "left")] = score_through_current_node
        if (i, j, "up") in unvisited_nodes:
            score_through_current_node = current_score + 1000
            if score_through_current_node < unvisited_nodes[(i, j, "up")]:
                unvisited_nodes[(i, j, "up")] = score_through_current_node
        if (i, j, "down") in unvisited_nodes:
            score_through_current_node = current_score + 1000
            if score_through_current_node < unvisited_nodes[(i, j, "down")]:
                unvisited_nodes[(i, j, "down")] = score_through_current_node
    if current_direction == "up":
        if (i - 1, j, "up") in unvisited_nodes:
            score_through_current_node = current_score + 1
            if score_through_current_node < unvisited_nodes[(i - 1, j, "up")]:
                unvisited_nodes[(i - 1, j, "up")] = score_through_current_node
        if (i, j, "right") in unvisited_nodes:
            score_through_current_node = current_score + 1000
            if score_through_current_node < unvisited_nodes[(i, j, "right")]:
                unvisited_nodes[(i, j, "right")] = score_through_current_node
        if (i, j, "left") in unvisited_nodes:
            score_through_current_node = current_score + 1000
            if score_through_current_node < unvisited_nodes[(i, j, "left")]:
                unvisited_nodes[(i, j, "left")] = score_through_current_node
    if current_direction == "down":
        if (i + 1, j, "down") in unvisited_nodes:
            score_through_current_node = current_score + 1
            if score_through_current_node < unvisited_nodes[(i + 1, j, "down")]:
                unvisited_nodes[(i + 1, j, "down")] = score_through_current_node
        if (i, j, "right") in unvisited_nodes:
            score_through_current_node = current_score + 1000
            if score_through_current_node < unvisited_nodes[(i, j, "right")]:
                unvisited_nodes[(i, j, "right")] = score_through_current_node
        if (i, j, "left") in unvisited_nodes:
            score_through_current_node = current_score + 1000
            if score_through_current_node < unvisited_nodes[(i, j, "left")]:
                unvisited_nodes[(i, j, "left")] = score_through_current_node

    """
    pick new current node, update current direction and score,
    and remove it from unvisited nodes.
    """
    visited_nodes[current_node] = current_score
    if unvisited_nodes:
        current_node = get_next_current_node(unvisited_nodes)
        current_score = unvisited_nodes[current_node]

"""
Next, go back through recursively and find all neighboring tiles whose
scores are equal to the minimum path score minus cost of getting there
"""


def get_tiles_on_path(current_node, tiles_on_path):

    i, j, current_direction = current_node

    if current_node == starting_node:
        return

    current_score = visited_nodes[current_node]

    if current_direction == "right":
        if (i, j - 1, "right") in visited_nodes:
            score_through_current_node = current_score - 1
            if score_through_current_node == visited_nodes[(i, j - 1, "right")]:
                tiles_on_path.add((i, j - 1))
                get_tiles_on_path((i, j - 1, "right"), tiles_on_path)

        if (i, j, "up") in visited_nodes:
            score_through_current_node = current_score - 1000
            if score_through_current_node == visited_nodes[(i, j, "up")]:
                get_tiles_on_path((i, j, "up"), tiles_on_path)

        if (i, j, "down") in visited_nodes:
            score_through_current_node = current_score - 1000
            if score_through_current_node == visited_nodes[(i, j, "down")]:
                get_tiles_on_path((i, j, "down"), tiles_on_path)

    if current_direction == "left":
        if (i, j + 1, "left") in visited_nodes:
            score_through_current_node = current_score - 1
            if score_through_current_node == visited_nodes[(i, j + 1, "left")]:
                tiles_on_path.add((i, j + 1))
                get_tiles_on_path((i, j + 1, "left"), tiles_on_path)

        if (i, j, "up") in visited_nodes:
            score_through_current_node = current_score - 1000
            if score_through_current_node == visited_nodes[(i, j, "up")]:
                get_tiles_on_path((i, j, "up"), tiles_on_path)

        if (i, j, "down") in visited_nodes:
            score_through_current_node = current_score - 1000
            if score_through_current_node == visited_nodes[(i, j, "down")]:
                get_tiles_on_path((i, j, "down"), tiles_on_path)

    if current_direction == "up":
        if (i + 1, j, "up") in visited_nodes:
            score_through_current_node = current_score - 1
            if score_through_current_node == visited_nodes[(i + 1, j, "up")]:
                tiles_on_path.add((i + 1, j))
                get_tiles_on_path((i + 1, j, "up"), tiles_on_path)

        if (i, j, "left") in visited_nodes:
            score_through_current_node = current_score - 1000
            if score_through_current_node == visited_nodes[(i, j, "left")]:
                get_tiles_on_path((i, j, "left"), tiles_on_path)

        if (i, j, "right") in visited_nodes:
            score_through_current_node = current_score - 1000
            if score_through_current_node == visited_nodes[(i, j, "right")]:
                get_tiles_on_path((i, j, "right"), tiles_on_path)
    if current_direction == "down":
        if (i - 1, j, "down") in visited_nodes:
            score_through_current_node = current_score - 1
            if score_through_current_node == visited_nodes[(i - 1, j, "down")]:
                tiles_on_path.add((i - 1, j))
                get_tiles_on_path((i - 1, j, "down"), tiles_on_path)

        if (i, j, "left") in visited_nodes:
            score_through_current_node = current_score - 1000
            if score_through_current_node == visited_nodes[(i, j, "left")]:
                get_tiles_on_path((i, j, "left"), tiles_on_path)

        if (i, j, "right") in visited_nodes:
            score_through_current_node = current_score - 1000
            if score_through_current_node == visited_nodes[(i, j, "right")]:
                get_tiles_on_path((i, j, "right"), tiles_on_path)

    return


tiles_on_path1 = set()
if visited_nodes[ending_node_up] <= visited_nodes[ending_node_right]:
    endingnode_ij = (ending_node_up[0], ending_node_up[1])
    tiles_on_path1 = {endingnode_ij}
    get_tiles_on_path(ending_node_up, tiles_on_path1)

tiles_on_path2 = set()
if visited_nodes[ending_node_right] <= visited_nodes[ending_node_up]:
    endingnode_ij = (ending_node_up[0], ending_node_up[1])
    tiles_on_path2 = {endingnode_ij}
    get_tiles_on_path(ending_node_right, tiles_on_path2)

print(len(tiles_on_path1 | tiles_on_path2))
