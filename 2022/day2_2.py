from helpers import loadFileByLine;

rounds = loadFileByLine('inputs/day2_1.txt')

# Rules:
# A = Rock (1 point)
# B = Paper (2 points)
# C = Scissors (3 points)
#
# X = Lose (0 points)
# Y = Draw (3 points)
# Z = Win (6 points)

result_points = {
    'X': 0,
    'Y': 3,
    'Z': 6
}

def getResultPoints(result):
    return result_points[result]

choice_points = {
    'AX': 3, # rock / lose: scissors
    'AY': 1, # rock / draw: rock
    'AZ': 2, # rock / win: paper
    'BX': 1, # paper / lose: rock
    'BY': 2, # paper / draw: paper
    'BZ': 3, # paper / win: scissors
    'CX': 2, # scissors / lose: paper
    'CY': 3, # scissors / draw: scissors
    'CZ': 1  # scissors / win: rock
}

def getChoicePoints(theirChoice, result):
    return choice_points[theirChoice + result]

total_points = 0
for round in rounds:
    [theirChoice, result] = round.split()
    points = getResultPoints(result) + getChoicePoints(theirChoice, result)
    total_points += points

print(total_points)