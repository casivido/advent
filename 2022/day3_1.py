from helpers import loadFileByLine;

rucksacks = loadFileByLine('inputs/day3_1.txt')

typePointsAtIndex = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def getTypePoints(type):
    return typePointsAtIndex.index(type) + 1

total_sum = 0
for sack in rucksacks:
    sack_half_length = int(len(sack)/2)
    first_half = sack[:sack_half_length]
    second_half = sack[sack_half_length:]


    types_found = {}
    for type in first_half:
        types_found[type] = True

    duplicate_type = None
    for type in second_half:
        if type in types_found:
            duplicate_type = type
            break

    total_sum += getTypePoints(duplicate_type)
print(total_sum)
