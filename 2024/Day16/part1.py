import numpy as np

# Dikjstra's algorithm!

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
    # I have learned from the subreddit that I really should use a priority queue instead. next time!
    min = np.inf
    for key in unvisited_nodes.keys():
        if unvisited_nodes[key][0] < min:
            min = unvisited_nodes[key][0]
            current_node = key
    return current_node


unvisited_nodes = {}
for i in range(n_rows):
    for j in range(n_cols):
        if maze[i, j] == "." or maze[i, j] == "E":
            unvisited_nodes[(i, j)] = (np.inf, None)  # score, direction
        elif maze[i, j] == "S":
            current_node = (i, j)
            unvisited_nodes[(i, j)] = (0, None)

current_direction = "right"
current_score = 0

while maze[current_node] != "E":
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
    current_node = get_next_current_node(unvisited_nodes)
    current_score = unvisited_nodes[current_node][0]
    current_direction = unvisited_nodes[current_node][1]


print(unvisited_nodes[current_node][0])
