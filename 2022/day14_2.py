from functools import cmp_to_key
from helpers import loadFileByLine;

rock_paths = loadFileByLine('inputs/day14_1.txt')
X = 0
Y = 1

def getCoordinatesFromLine(line):
    coordinates_raw = line.split(' -> ')
    coordinates = list(map(lambda x: list(map(int, x.split(','))), coordinates_raw))
    return coordinates

path_list = list(map(getCoordinatesFromLine, rock_paths))

starting_sand_location = [500,0]
x_range = [starting_sand_location[X], starting_sand_location[X]]
y_range = [starting_sand_location[Y], starting_sand_location[Y]]
for path in path_list:
    for coordinate in path:
        if coordinate[X] < x_range[0]:
            x_range[0] = coordinate[X]
        elif coordinate[X] > x_range[1]:
            x_range[1] = coordinate[X]
        if coordinate[Y] < y_range[0]:
            y_range[0] = coordinate[Y]
        elif coordinate[Y] > y_range[1]:
            y_range[1] = coordinate[Y]

for path in path_list:
    for coordinate in path:
        coordinate[X] -= x_range[0]
        coordinate[Y] -= y_range[0]

starting_sand_location[X] -= x_range[0]
starting_sand_location[Y] -= y_range[0]
x_range[1] -= x_range[0]
x_range[0] = 0
y_range[1] -= y_range[0]
y_range[0] = 0

height = y_range[1] + 3
min_x = 0
max_x = height * 2

# how many tiles to move things to the right
x_tiles_needed = max(0, height - starting_sand_location[X])

# make sure map is wide enough
x_range[1] = max(x_range[1], max_x)

# move things to the right
for path in path_list:
    for coordinate in path:
        coordinate[X] += x_tiles_needed
starting_sand_location[X] += x_tiles_needed

coordinate_pairs = []
for path in path_list:
    counter = 0
    while counter + 1 < len(path):
        coordinate_pairs.append([path[counter], path[counter+1]])
        counter += 1

rock_map = []
for y in range(y_range[1]+3):
    rock_map.append([])
    character_to_add = '.' if y != y_range[1]+2 else '#'
    for x in range(x_range[1]+1):
        rock_map[y].append(character_to_add)

# add rocks
for pair in coordinate_pairs:
    first = pair[0]
    second = pair[1]
    pair_x_range = [min(first[X], second[X]), max(first[X], second[X])]
    pair_y_range = [min(first[Y], second[Y]), max(first[Y], second[Y])]

    x_counter = pair_x_range[0]
    y_counter = pair_y_range[0]
    while x_counter <= pair_x_range[1]:
        while y_counter <= pair_y_range[1]:
            rock_map[y_counter][x_counter] = '#'
            y_counter += 1
        x_counter += 1

    x_counter = pair_x_range[0]
    y_counter = pair_y_range[0]
    while y_counter <= pair_y_range[1]:
        while x_counter <= pair_x_range[1]:
            rock_map[y_counter][x_counter] = '#'
            x_counter += 1
        y_counter += 1

def inMap(location):
    x,y  = location
    within_x = 0 <= x < len(rock_map[0]) # assumes rectangle shape
    within_y = 0 <= y < len(rock_map)
    if within_x and within_y:
        return True
    else:
        return False

def get_final_location(starting_location):
    try_locations = [
        [starting_location[X], starting_location[Y]+1],
        [starting_location[X]-1, starting_location[Y]+1],
        [starting_location[X]+1, starting_location[Y]+1]
    ]
    for potential_location in try_locations:
        if not inMap(potential_location):
            return potential_location
        if rock_map[potential_location[Y]][potential_location[X]] == '.':
            return get_final_location(potential_location)
    return starting_location

sand_counter = 0
while True:
    end_location = get_final_location(starting_sand_location)
    if inMap(end_location):
        rock_map[end_location[Y]][end_location[X]] = '+'
        sand_counter += 1
        if end_location[X] == starting_sand_location[X] and end_location[Y] == starting_sand_location[Y]:
            break
    else:
        break

print('Sand Counter: ', sand_counter)