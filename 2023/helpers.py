def loadFileByLine(filename):
    with open(filename, 'r') as input:
        instructions = [line.strip() for line in input.readlines()]
    return instructions;