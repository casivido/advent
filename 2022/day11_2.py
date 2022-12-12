import time
from functools import reduce
from helpers import loadFileByLine;

instructions = loadFileByLine('inputs/day11_1.txt')


items = []
divisors = []
def read_monkey(input_lines, monkey_index):
    arg1, op, arg2 = input_lines[2][17:].split(' ')
    item_values = list(map(int, input_lines[1][16:].split(', ')))
    item_indices = []
    divisor = int(input_lines[3][18:])
    divisors.append(divisor)
    for item_value in item_values:
        items.append({ 'value': item_value, 'history': [monkey_index] })
        item_indices.append(len(items) - 1)
    return {
        'items': item_indices,
        'arg1': arg1,
        'arg2': arg2,
        'op': op,
        'divisible_num': divisor,
        'true_monkey': int(input_lines[4][24:]),
        'false_monkey': int(input_lines[5][25:]),
        'inspected_count': 0
    }

# read input
monkeys = []
cur_input_line = 0
lines_per_monkey = 7
while cur_input_line < len(instructions):
    monkeys.append(read_monkey(instructions[cur_input_line:cur_input_line+lines_per_monkey], len(monkeys)))
    cur_input_line += lines_per_monkey

num_monkeys = len(monkeys)

times = {
    'setting_up': 0,
    'multiply': 0,
    'add': 0,
    'mod': 0,
    'square': 0
}
indices = set([])
def run_round():
    cur_monkey_index = 0
    div_product = reduce(lambda x,y: x*y, divisors)
    while cur_monkey_index < num_monkeys:
        cur_monkey = monkeys[cur_monkey_index]
        for index in cur_monkey['items']:
            timer = time.time()
            cur_monkey['inspected_count'] += 1
            arg1 = items[index] if cur_monkey['arg1'] == 'old' else { 'value': int(cur_monkey['arg1']) }
            arg2 = items[index] if cur_monkey['arg2'] == 'old' else { 'value': int(cur_monkey['arg2']) }
            op = cur_monkey['op']
            times['setting_up'] += time.time() - timer
            timer = time.time()
            if op == '*':
                if cur_monkey['arg1'] == 'old' and cur_monkey['arg2'] == 'old':
                    items[index]['value'] = pow(arg1['value'], 2)% div_product## YES
                    times['square'] += time.time() - timer
                    timer = time.time()
                else:
                    items[index]['value'] = (arg1['value'] * arg2['value'])% div_product ## YES
                    times['multiply'] += time.time() - timer
                    timer = time.time()
            elif op == '+':
                items[index]['value'] = arg1['value'] + arg2['value'] ## LESS MAYBE
                times['add'] += time.time() - timer
                timer = time.time()
            if (items[index]['value'] % cur_monkey['divisible_num']) == 0: # MAYBE
                monkeys[cur_monkey['true_monkey']]['items'].append(index)
                items[index]['history'].append(cur_monkey['true_monkey'])
            else:
                monkeys[cur_monkey['false_monkey']]['items'].append(index)
                items[index]['history'].append(cur_monkey['false_monkey'])
            times['mod'] += time.time() - timer
            timer = time.time()
        cur_monkey['items'] = []
        cur_monkey_index += 1

# run rounds
num_rounds = 10000
for round in range(num_rounds):
    print(round)
    run_round()

# get active monkeys
sorted_inspection_counts = list(map(lambda monkey: monkey['inspected_count'], monkeys))
sorted_inspection_counts.sort(reverse = True)
print(sorted_inspection_counts)
print('answer:', sorted_inspection_counts[0] * sorted_inspection_counts[1])
print(items)
print(times)