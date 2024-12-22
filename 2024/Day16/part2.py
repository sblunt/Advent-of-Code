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
        if unvisited_nodes[key][0] < min:
            min = unvisited_nodes[key][0]
            current_node = key
    return current_node


unvisited_nodes = {}
visited_nodes = {}
for i in range(n_rows):
    for j in range(n_cols):
        if maze[i, j] == ".":
            unvisited_nodes[(i, j)] = (np.inf, None)  # score, direction
        if maze[i, j] == "E":
            unvisited_nodes[(i, j)] = (np.inf, None)
            ending_node = (i, j)
        elif maze[i, j] == "S":
            current_node = (i, j)
            unvisited_nodes[(i, j)] = (0, None)
            starting_node = (i, j)

current_direction = "right"
current_score = 0

while unvisited_nodes:
    if current_direction == "right":
        right_cost = 1
        left_cost = 2001
        up_cost = 1001
        down_cost = 1001
    elif current_direction == "left":
        right_cost = 2001
        left_cost = 1
        up_cost = 1001
        down_cost = 1001
    elif current_direction == "up":
        right_cost = 1001
        left_cost = 1001
        up_cost = 1
        down_cost = 2001
    elif current_direction == "down":

        right_cost = 1001
        left_cost = 1001
        up_cost = 2001
        down_cost = 1

    i, j = current_node
    del unvisited_nodes[current_node]

    """
    update neighbor node scores
    """

    # check if position to the left is in unvisited nodes; if so, update its score
    # through current node
    if (i, j - 1) in unvisited_nodes:
        score_through_current_node = current_score + left_cost
        if score_through_current_node < unvisited_nodes[(i, j - 1)][0]:
            unvisited_nodes[(i, j - 1)] = (score_through_current_node, "left")

    # check if position to the right is in unvisited nodes; if so, update its score
    # through current node
    if (i, j + 1) in unvisited_nodes:
        score_through_current_node = current_score + right_cost
        if score_through_current_node < unvisited_nodes[(i, j + 1)][0]:
            unvisited_nodes[(i, j + 1)] = (score_through_current_node, "right")

    # check if position up is in unvisited nodes; if so, update its score
    # through current node
    if (i - 1, j) in unvisited_nodes:
        score_through_current_node = current_score + up_cost
        if score_through_current_node < unvisited_nodes[(i - 1, j)][0]:
            unvisited_nodes[(i - 1, j)] = (score_through_current_node, "up")

    # check if position down is in unvisited nodes; if so, update its score
    # through current node
    if (i + 1, j) in unvisited_nodes:
        score_through_current_node = current_score + down_cost
        if score_through_current_node < unvisited_nodes[(i + 1, j)][0]:
            unvisited_nodes[(i + 1, j)] = (score_through_current_node, "down")

    """
    pick new current node, update current direction and score,
    and remove it from unvisited nodes.
    """
    visited_nodes[current_node] = current_score
    if unvisited_nodes:
        current_node = get_next_current_node(unvisited_nodes)
        current_score = unvisited_nodes[current_node][0]
        current_direction = unvisited_nodes[current_node][1]


print(visited_nodes[ending_node])


"""
Next, go back through recursively and find all neighboring tiles whose
scores are equal to the minimum path score minus cost of getting there
"""


def get_tiles_on_path(
    visited_nodes, current_node, current_node_score, current_direction
):

    i, j = current_node

    if current_node_score == 0:
        return [current_node]
    else:

        up_node = (i - 1, j)
        up_node_score = np.inf
        down_node = (i + 1, j)
        down_node_score = np.inf
        left_node = (i, j - 1)
        left_node_score = np.inf
        right_node = (i, j + 1)
        right_node_score = np.inf
        if up_node in visited_nodes:
            up_node_score = visited_nodes[up_node]
        if down_node in visited_nodes:
            down_node_score = visited_nodes[down_node]
        if left_node in visited_nodes:
            left_node_score = visited_nodes[left_node]
        if right_node in visited_nodes:
            right_node_score = visited_nodes[right_node]

        up_path = []
        down_path = []
        right_path = []
        left_path = []

        if current_direction == "up":

            if down_node_score == current_node_score - 1:
                down_path = get_tiles_on_path(
                    visited_nodes, down_node, down_node_score, "up"
                )
                down_path.append(current_node)
            if down_node_score == current_node_score - 1001:
                down_path1 = get_tiles_on_path(
                    visited_nodes, down_node, down_node_score, "left"
                )
                down_path2 = get_tiles_on_path(
                    visited_nodes, down_node, down_node_score, "right"
                )
                down_path3 = get_tiles_on_path(
                    visited_nodes, down_node, current_node_score - 1, "up"
                )

                down_path = down_path1 + down_path2 + down_path3 + [current_node]
        if current_direction == "down":

            if up_node_score == current_node_score - 1:
                up_path = get_tiles_on_path(
                    visited_nodes, up_node, up_node_score, "down"
                )
                up_path.append(current_node)
            if up_node_score == current_node_score - 1001:
                up_path1 = get_tiles_on_path(
                    visited_nodes, up_node, up_node_score, "left"
                )
                up_path2 = get_tiles_on_path(
                    visited_nodes, up_node, up_node_score, "right"
                )
                up_path3 = get_tiles_on_path(
                    visited_nodes, up_node, current_node_score - 1, "up"
                )
                up_path = up_path1 + up_path2 + up_path3 + [current_node]
        if current_direction == "right":

            if left_node_score == current_node_score - 1:
                right_path = get_tiles_on_path(
                    visited_nodes, left_node, left_node_score, "right"
                )
                right_path.append(current_node)
            if left_node_score == current_node_score - 1001:
                right_path1 = get_tiles_on_path(
                    visited_nodes, left_node, left_node_score, "up"
                )
                right_path2 = get_tiles_on_path(
                    visited_nodes, left_node, left_node_score, "down"
                )
                right_path3 = get_tiles_on_path(
                    visited_nodes, left_node, current_node_score - 1, "right"
                )

                right_path = right_path1 + right_path2 + right_path3 + [current_node]
        if current_direction == "left":

            if right_node_score == current_node_score - 1:
                left_path = get_tiles_on_path(
                    visited_nodes, right_node, right_node_score, "left"
                )
                left_path.append(current_node)
            if right_node_score == current_node_score - 1001:
                left_path1 = get_tiles_on_path(
                    visited_nodes, right_node, right_node_score, "up"
                )
                left_path2 = get_tiles_on_path(
                    visited_nodes, right_node, right_node_score, "down"
                )
                left_path3 = get_tiles_on_path(
                    visited_nodes, right_node, current_node_score - 1, "left"
                )
                left_path = left_path1 + left_path2 + left_path3 + [current_node]

        return down_path + up_path + left_path + right_path


all_tiles_on_best_paths1 = get_tiles_on_path(
    visited_nodes,
    ending_node,
    visited_nodes[ending_node],
    "up",
)

all_tiles_on_best_paths2 = get_tiles_on_path(
    visited_nodes,
    ending_node,
    visited_nodes[ending_node],
    "right",
)

best_tiles = set(all_tiles_on_best_paths1 + all_tiles_on_best_paths2)
print(best_tiles)
# print(len(best_tiles))
