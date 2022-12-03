from helpers import loadFileByLine;

rucksacks = loadFileByLine('inputs/day3_1.txt')

typePointsAtIndex = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def getTypePoints(type):
    return typePointsAtIndex.index(type) + 1

counter = 0
total_sum = 0
while counter < len(rucksacks):
    sack1 = rucksacks[counter]
    sack2 = rucksacks[counter+1]
    sack3 = rucksacks[counter+2]

    first_types_found = {}
    for type in sack1:
        first_types_found[type] = True

    second_types_found = {}
    for type in sack2:
        second_types_found[type] = True

    duplicate_type = None
    for type in sack3:
        if type in sack1 and type in sack2:
            duplicate_type = type
            break

    print(duplicate_type)

    total_sum += getTypePoints(duplicate_type)
    counter += 3
print(total_sum)
