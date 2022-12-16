import re
import time
from functools import cmp_to_key
from helpers import loadFileByLine;

sensor_data_raw_list = loadFileByLine('inputs/day15_1.txt')
# chosen_y = 10 # input test

map_blank_spans = {} # dict of each y, containing tuples for spans of blank spots

X = 0
Y = 1

def partially_collapse_tuple_spans(tuple_spans):
    collapsed_spans = []
    used_counters = []
    first_counter = 0
    while first_counter < len(tuple_spans):
        if first_counter in used_counters: # don't collapse the same tuple multiple times
            first_counter += 1
            continue
        first_span = tuple_spans[first_counter]
        second_counter = first_counter + 1
        new_span = first_span
        while second_counter < len(tuple_spans):
            if second_counter in used_counters: # don't collapse the same tuple multiple times
                second_counter += 1
                continue
            second_span = tuple_spans[second_counter]
            collapse = False
            if second_span[0] <= first_span[0] <= second_span[1]:
                new_span = (second_span[0], max(first_span[1], second_span[1]))
                collapse = True
            elif first_span[0] <= second_span[0] <= first_span[1]:
                new_span = (first_span[0], max(first_span[1], second_span[1]))
                collapse = True
            elif first_span[1] + 1 == second_span[0]:
                new_span = (first_span[0], second_span[1])
                collapse = True
            elif second_span[1] + 1 == first_span[0]:
                new_span = (second_span[0], first_span[1])
                collapse = True
            if collapse:
                used_counters.append(second_counter)
                break
            second_counter += 1
        collapsed_spans.append(new_span)
        first_counter += 1
    return collapsed_spans

# reformat the raw input
timer = time.time()
sensor_data_list = []
for sensor_data_raw in sensor_data_raw_list:
    sensor_x, sensor_y, beacon_x, beacon_y = list(map(int, re.search(r".*=(-?\d*), y=(-?\d*):.*=(-?\d*), y=(-?\d*)", sensor_data_raw).groups()))
    sensor_data_list.append([[sensor_x, sensor_y], [beacon_x, beacon_y], [abs(sensor_x-beacon_x), abs(sensor_y-beacon_y)]])
print('read_data_time: ', time.time() - timer)
timer = time.time()

# iterate over sensors and mark off the chosen y vector
for sensor_data in sensor_data_list:
    sensor, beacon, beacon_distance = sensor_data

    total_beacon_distance = beacon_distance[X] + beacon_distance[Y]
    min_y = sensor[Y]-total_beacon_distance
    max_y = sensor[Y]+total_beacon_distance
    for y in range(min_y,max_y+1):
        x_diff = total_beacon_distance-abs(sensor[Y]-y)
        min_x = sensor[X]-x_diff
        max_x = sensor[X]+x_diff
        if y not in map_blank_spans:
            map_blank_spans[y] = [(min_x, max_x)]
        else:
            map_blank_spans[y].append((min_x, max_x))
            map_blank_spans[y] = partially_collapse_tuple_spans(map_blank_spans[y])
print('span creation: ', time.time() - timer)
timer = time.time()

collapsed_spans_dict = {}
# collapse tuples
for y, tuple_spans in map_blank_spans.items():
    previous_length = len(tuple_spans)
    collapsing_spans = tuple_spans
    while True:
        collapsing_spans = partially_collapse_tuple_spans(collapsing_spans)
        if len(collapsing_spans) == previous_length:
            collapsed_spans_dict[y] = collapsing_spans
            break
        previous_length = len(collapsing_spans)
    collapsing_spans.sort(key=lambda x: x[0])
print('collapsing spans time: ', time.time() - timer)
timer = time.time()

# parse through spans
max_beacon = 20 # test
max_beacon = 4000000 # prod
x_answer = None
y_answer = None
for y, spans in collapsed_spans_dict.items():
    if 0 <= y <= max_beacon:
        counter = 0
        while (counter + 1) < len(spans):
            x_gap = spans[counter][1]+1
            if 0 <= x_gap <= max_beacon:
                print('x: ', x_gap, 'y: ', y)
                x_answer = x_gap
                y_answer = y
                break
            x_gap = spans[counter+1][0]-1
            if 0 <= x_gap <= max_beacon:
                print('x: ', x_gap, 'y: ', y)
                x_answer = x_gap
                y_answer = y
                break

            counter += 1
print('parsing spans time: ', time.time() - timer)
print('answer: ', x_answer * 4000000 + y_answer)

# OUTPUT: debug runs roughly 8.5x slower
# └─ $ python3 day15_2.py
# read_data_time:  0.00031304359436035156
# span creation:  64.24702310562134
# collapsing spans time:  14.377575397491455
# x:  3292963 y:  3019123
# parsing spans time:  0.8820540904998779
# answer:  13171855019123