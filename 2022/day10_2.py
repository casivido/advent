from helpers import loadFileByLine;

instructions = loadFileByLine('inputs/day10_1.txt')

cycle = 0
register_x = 1
signal_strengths = []
screen = []
def run_cycle():
    global cycle
    print(cycle)
    line_number = int(cycle/40)
    column_number = cycle%40
    sprite_in_view = column_number >= register_x - 1 and column_number <= register_x + 1
    character = '#' if sprite_in_view else '.'
    if column_number == 0:
        screen.append("")
    screen[line_number] += character
    cycle += 1

for instruction in instructions:
    instructions_raw = instruction.split(' ')
    command = instructions_raw[0]

    run_cycle()
    if command == "addx":
        run_cycle()
        value = int(instructions_raw[1])
        register_x += value

for line in screen:
    print(line)