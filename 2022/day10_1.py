from helpers import loadFileByLine;

instructions = loadFileByLine('inputs/day10_1.txt')

cycle = 1
register_x = 1
signal_strengths = []
ran_2 = False
for instruction in instructions:
    instructions_raw = instruction.split(' ')
    command = instructions_raw[0]

    if (cycle+20)%40 == 0:
        signal_strengths.append(cycle*register_x)
        print(cycle, signal_strengths[-1])
    if command == "addx":
        ran_2 = True
        value = int(instructions_raw[1])
        if (cycle+21)%40 == 0:
            signal_strengths.append((cycle+1)*register_x)
            print(cycle+1, signal_strengths[-1])
        register_x += value
        cycle += 2
    elif command == "noop":
        cycle += 1
    else:
        print("error")
        print(instruction)
        print(command)

print(cycle)
print(sum(signal_strengths))