import re
from functools import cmp_to_key
from helpers import loadFileByLine;

sensor_data_raw_list = loadFileByLine('inputs/day15_1.txt')
# chosen_y = 10 # input test
chosen_y = 2000000 # input 1
y_data = {} # { x: B/S/#}

X = 0
Y = 1

# reformat the raw input
sensor_data_list = []
for sensor_data_raw in sensor_data_raw_list:
    sensor_x, sensor_y, beacon_x, beacon_y = list(map(int, re.search(r".*=(-?\d*), y=(-?\d*):.*=(-?\d*), y=(-?\d*)", sensor_data_raw).groups()))
    sensor_data_list.append([[sensor_x, sensor_y], [beacon_x, beacon_y], [abs(sensor_x-beacon_x), abs(sensor_y-beacon_y)]])

# iterate over sensors and mark off the chosen y vector
for sensor_data in sensor_data_list:
    sensor, beacon, beacon_distance = sensor_data
    if beacon[Y] == chosen_y:
        y_data[beacon[X]] = 'B'

    distance_from_chosen_y = abs(chosen_y - sensor[Y])
    overkill = beacon_distance[X] + beacon_distance[Y] - distance_from_chosen_y

    if overkill >= 0:
        starting_x = sensor[X] - overkill
        ending_x = sensor[X] + overkill
        for x in range(starting_x, ending_x+1):
            if x not in y_data:
                y_data[x] = '#'

# count blank spots in chosen y for solution answer
blank_counter = 0
for x, value in y_data.items():
    if value == '#':
        blank_counter += 1
print(blank_counter)