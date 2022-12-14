import ast
import time
from functools import cmp_to_key
from helpers import loadFileByLine;

VALID = 1
INVALID = 2
DUNNO = 3

pairs_raw = loadFileByLine('inputs/day13_1.txt')

counter = 0
lines = [[[2]],[[6]]]
while counter+1 < len(pairs_raw):
    # print(pairs_raw[counter], pairs_raw[counter+1])
    lines.append(ast.literal_eval(pairs_raw[counter]))
    lines.append(ast.literal_eval(pairs_raw[counter+1]))
    counter += 3

def compare_elements(first, second):
    if type(first) is list and type(second) is list:
        counter = 0
        while True:
            if counter == len(first) and counter == len(second):
                return DUNNO
            if counter < len(first) and counter == len(second):
                return INVALID
            if counter == len(first) and counter < len(second):
                return VALID
            result = compare_elements(first[counter], second[counter])
            if result != DUNNO:
                return result
            else:
                counter += 1
    elif type(first) is list and type(second) is not list:
        return compare_elements(first, [second])
    elif type(second) is list and type(first) is not list:
        return compare_elements([first], second)
    else:
        if first < second:
            return VALID
        elif first > second:
            return INVALID
    return DUNNO

results = []
for line in lines:
    results.append([])

for first_index, first_line in enumerate(lines):
    for second_index, second_line in enumerate(lines):
        if first_index == second_index:
            results[first_index].append('myself')
        else:
            results[first_index].append(compare_elements(lines[first_index], lines[second_index]))

# followers = []
# for index, line_results in enumerate(results):
#     followers.append({
#         'line_index': index,
#         'follower_indices': [n for n in list(range(len(line_results))) if line_results[n] == VALID]
#     })

# followers.sort(key=lambda x: len(x['follower_indices']))

def put_in_order(cur_list, remaining_indices):
    if len(remaining_indices) == 0:
        print(cur_list)
        return VALID
    if(len(cur_list) == 2):
        print('another round')
    for counter in range(len(remaining_indices)):
        remaining_index = remaining_indices[counter]
        if results[cur_list[-1]][remaining_index] == VALID:
            remaining_indices.pop(counter)
            if put_in_order(cur_list+[remaining_index], remaining_indices) == VALID:
                return VALID
            remaining_indices.insert(counter, remaining_index)
    return INVALID

all_indices = range(len(lines))
for index, line in enumerate(lines):
    timer = time.time()
    print(index)
    other_indices = [n for n in all_indices if n != index]
    if index == 12:
        print('here we go')
    print(index, put_in_order([index], other_indices), timer - time.time())