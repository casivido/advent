import re
from helpers import loadFileByLine;

instructions = loadFileByLine('inputs/day11_1.txt')

def read_monkey(input_lines):
    arg1, op, arg2 = input_lines[2][17:].split(' ')
    return {
        'items': list(map(int, input_lines[1][16:].split(', '))),
        'arg1': arg1,
        'arg2': arg2,
        'op': op,
        'divisible_num': int(input_lines[3][18:]),
        'true_monkey': int(input_lines[4][24:]),
        'false_monkey': int(input_lines[5][25:]),
        'inspected_count': 0
    }

# read input
monkeys = []
cur_input_line = 0
lines_per_monkey = 7
while cur_input_line < len(instructions):
    monkeys.append(read_monkey(instructions[cur_input_line:cur_input_line+lines_per_monkey]))
    cur_input_line += lines_per_monkey

num_monkeys = len(monkeys)
def run_round():
    cur_monkey_index = 0
    while cur_monkey_index < num_monkeys:
        cur_monkey = monkeys[cur_monkey_index]
        for worry_level in cur_monkey['items']:
            cur_monkey['inspected_count'] += 1
            arg1 = worry_level if cur_monkey['arg1'] == 'old' else int(cur_monkey['arg1'])
            arg2 = worry_level if cur_monkey['arg2'] == 'old' else int(cur_monkey['arg2'])
            op = cur_monkey['op']
            if op == '*':
                new_worry_level = arg1 * arg2
            elif op == '+':
                new_worry_level = arg1 + arg2
            new_worry_level = int(new_worry_level/3)
            if (new_worry_level / cur_monkey['divisible_num']).is_integer():
                monkeys[cur_monkey['true_monkey']]['items'].append(new_worry_level)
            else:
                monkeys[cur_monkey['false_monkey']]['items'].append(new_worry_level)
        cur_monkey['items'] = []
        cur_monkey_index += 1



# run rounds
num_rounds = 20
for round in range(num_rounds):
    run_round()

# get active monkeys
sorted_inspection_counts = list(map(lambda monkey: monkey['inspected_count'], monkeys))
sorted_inspection_counts.sort(reverse = True)
print(sorted_inspection_counts[0] * sorted_inspection_counts[1])

print('done')