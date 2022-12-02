from helpers import loadFileByLine;

rounds = loadFileByLine('inputs/day2_1.txt')

# Rules:
# A, X = Rock
# B, Y = Paper
# C, Z = Scissors

choice_points = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

def getChoicePoints(choice):
    return choice_points[choice]

outcome_points = {
    'AX': 3, # rock / rock
    'AY': 6, # rock / paper
    'AZ': 0, # rock / scissors
    'BX': 0, # paper / rock
    'BY': 3, # paper / paper
    'BZ': 6, # paper / scissors
    'CX': 6, # scissors / rock
    'CY': 0, # scissors / paper
    'CZ': 3  # scissors / scissors
}

def getOutcomePoints(theirChoice, yourChoice):
    return outcome_points[theirChoice + yourChoice]

total_points = 0
for round in rounds:
    [them, you] = round.split()
    points = getChoicePoints(you) + getOutcomePoints(them, you)
    total_points += points

print(total_points)