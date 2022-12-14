import ast
from helpers import loadFileByLine;

VALID = 1
INVALID = 2
DUNNO = 3

pairs_raw = loadFileByLine('inputs/day13_1.txt')

counter = 0
pairs = []
while counter+1 < len(pairs_raw):
    # print(pairs_raw[counter], pairs_raw[counter+1])
    pairs.append([ast.literal_eval(pairs_raw[counter]), ast.literal_eval(pairs_raw[counter+1])])
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

valid_indices = []
for index, pair in enumerate(pairs):
    if compare_elements(pair[0],pair[1]) == VALID:
        valid_indices.append(index+1)
print(sum(valid_indices))
