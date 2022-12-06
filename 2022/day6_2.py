import re
from helpers import loadFileByLine;

input = list(loadFileByLine('inputs/day6_1.txt')[0])

amount_unique = 14
running_letters = input[:amount_unique]
remaining_input = input[amount_unique:]

# https://stackoverflow.com/questions/5278122/checking-if-all-elements-in-a-list-are-unique
def unique_values(g):
    s = set()
    for x in g:
        if x in s: return False
        s.add(x)
    return True

counter = amount_unique
for letter in remaining_input:
    if unique_values(running_letters):
        break
    running_letters.pop(0)
    running_letters.append(letter)

    counter += 1

print(running_letters)
print(counter)