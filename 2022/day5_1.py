import re
from helpers import loadFileByLine;

instructions = loadFileByLine('inputs/day5_1.txt')

stacks = [
    ['F', 'H', 'B', 'V', 'R', 'Q', 'D', 'P'],
    ['L', 'D', 'Z', 'Q', 'W', 'V'],
    ['H', 'L', 'Z', 'Q', 'G', 'R', 'P', 'C'],
    ['R', 'D', 'H', 'F', 'J', 'V', 'B'],
    ['Z', 'W', 'L', 'C'],
    ['J', 'R', 'P', 'N', 'T', 'G', 'V', 'M'],
    ['J', 'R', 'L', 'V', 'M', 'B', 'S'],
    ['D','P','J'],
    ['D','C','N','W','V']
]

for step in instructions:
    print(step)
    [amount, source_stack_index, dest_stack_index] = map(lambda x: int(x), re.search(r"move (\d*) from (\d*) to (\d*)", step).groups())

    source_stack = stacks[source_stack_index-1]
    dest_stack = stacks[dest_stack_index-1]
    print(source_stack)
    print(dest_stack)
    start_index = len(source_stack)-amount

    crates_to_move = source_stack[start_index:]
    crates_to_move.reverse()

    source_stack = source_stack[:start_index]
    stacks[source_stack_index-1] = source_stack

    dest_stack = dest_stack + crates_to_move
    stacks[dest_stack_index-1] = dest_stack
    print(source_stack)
    print(dest_stack)

for stack in stacks:
    print(stack[-1])