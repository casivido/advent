from helpers import loadFileByLine;

instructions = loadFileByLine('inputs/day9_1.txt')

knot_positions = []
num_knots = 10
for num in range(num_knots):
    knot_positions.append({
        'x': 0,
        'y': 0
    })


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

def move_knot(leader, follower):
    if follower['x'] > (leader['x'] + 1):
        follower['x'] -= 1
        if follower['y'] > (leader['y']):
            follower['y'] -= 1
        if follower['y'] < (leader['y']):
            follower['y'] += 1
    if follower['x'] < (leader['x'] - 1):
        follower['x'] += 1
        if follower['y'] > (leader['y']):
            follower['y'] -= 1
        if follower['y'] < (leader['y']):
            follower['y'] += 1
    if follower['y'] > (leader['y'] + 1):
        follower['y'] -= 1
        if follower['x'] > (leader['x']):
            follower['x'] -= 1
        if follower['x'] < (leader['x']):
            follower['x'] += 1
    if follower['y'] < (leader['y'] - 1):
        follower['y'] += 1
        if follower['x'] > (leader['x']):
            follower['x'] -= 1
        if follower['x'] < (leader['x']):
            follower['x'] += 1

def take_step():
    direction_data = direction_list[current_direction]
    knot_positions[0][direction_data['axis']] += direction_data['value']

    for knot_num in range(num_knots)[1:]:
        leader = knot_positions[knot_num-1]
        follower = knot_positions[knot_num]
        move_knot(leader, follower)


    visited_tail_locations[f"{knot_positions[-1]['x']},{knot_positions[-1]['y']}"] = True

for instruction in instructions:
    current_direction, num_steps = instruction.split(' ')
    steps_left = int(num_steps)
    while steps_left != 0:
        take_step()
        steps_left -= 1

print(visited_tail_locations)
print(len(visited_tail_locations))