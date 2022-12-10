from helpers import loadFileByLine;

forest_heights = loadFileByLine("inputs/day8_1.txt")
forest_width = len(forest_heights) # square forest

def count_trees(axis, increment, cur_location):
    max_height = int(forest_heights[cur_location['y']][cur_location['x']])
    tree_counter = 0
    cur_location[axis] += increment
    while cur_location[axis] < forest_width and cur_location[axis] >= 0:
        tree_counter += 1
        cur_tree_height = int(forest_heights[cur_location['y']][cur_location['x']])
        if cur_tree_height >= max_height:
            break
        cur_location[axis] += increment
    return tree_counter

max_score = 0
for x in range(forest_width):
    for y in range(forest_width):
        up = count_trees('y', -1, {'x': x, 'y': y})
        down = count_trees('y', 1, {'x': x, 'y': y})
        left = count_trees('x', -1, {'x': x, 'y': y})
        right = count_trees('x', 1, {'x': x, 'y': y})

        score = up * down * left * right
        if score > max_score:
            max_score = score


print(max_score)