from helpers import loadFileByLine;

instructions = loadFileByLine('inputs/day9_1.txt')

head_position = {
    'x': 0,
    'y': 0
}

tail_position = {
    'x': 0,
    'y': 0
}

visited_tail_locations = {
    "0,0": True
}

direction_list = {
    'U': {
        "axis": 'y',
        "value": 1
    },
    'D': {
        "axis": 'y',
        "value": -1
    },
    'L': {
        "axis": 'x',
        "value": -1
    },
    'R': {
        "axis": 'x',
        "value": 1
    }
}

current_direction = None # U,D,L,R

def take_step():
    direction_data = direction_list[current_direction]
    head_position[direction_data['axis']] += direction_data['value']

    if tail_position['x'] > (head_position['x'] + 1):
        tail_position['x'] -= 1
        if tail_position['y'] > (head_position['y']):
            tail_position['y'] -= 1
        if tail_position['y'] < (head_position['y']):
            tail_position['y'] += 1
    if tail_position['x'] < (head_position['x'] - 1):
        tail_position['x'] += 1
        if tail_position['y'] > (head_position['y']):
            tail_position['y'] -= 1
        if tail_position['y'] < (head_position['y']):
            tail_position['y'] += 1
    if tail_position['y'] > (head_position['y'] + 1):
        tail_position['y'] -= 1
        if tail_position['x'] > (head_position['x']):
            tail_position['x'] -= 1
        if tail_position['x'] < (head_position['x']):
            tail_position['x'] += 1
    if tail_position['y'] < (head_position['y'] - 1):
        tail_position['y'] += 1
        if tail_position['x'] > (head_position['x']):
            tail_position['x'] -= 1
        if tail_position['x'] < (head_position['x']):
            tail_position['x'] += 1

    visited_tail_locations[f"{tail_position['x']},{tail_position['y']}"] = True

for instruction in instructions:
    current_direction, num_steps = instruction.split(' ')
    steps_left = int(num_steps)
    while steps_left != 0:
        take_step()
        steps_left -= 1

print(visited_tail_locations)
print(len(visited_tail_locations))