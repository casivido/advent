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

followers = []
for index, line_results in enumerate(results):
    followers.append([n for n in list(range(len(line_results))) if line_results[n] == VALID])

last_index = 6 #test
last_index = 151 #prod TODO: find this dynamically by getting the index with no followers
excluded_indices = [last_index]
def getPrecedingIndex(follower_index):
    for potential_leader_index, followers_list in enumerate(followers):
        found = False
        too_many = False
        for prospect_follower_index in followers_list:
            if prospect_follower_index == follower_index:
                found = True
            elif prospect_follower_index not in excluded_indices:
                too_many = True
        if found and not too_many:
            excluded_indices.append(potential_leader_index)
            return getPrecedingIndex(potential_leader_index)


getPrecedingIndex(last_index)
excluded_indices.reverse()
print(excluded_indices)
print('found: ', len(excluded_indices))
print('total: ', len(lines))

for index in excluded_indices:
    print(lines[index])
first = excluded_indices.index(0)+1
second = excluded_indices.index(1)+1
print('answer: ', first*second)
