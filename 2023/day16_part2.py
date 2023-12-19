from helpers import loadFileByLine

import pprint
print = pprint.PrettyPrinter(indent=2).pprint

DIRECTION_VECTORS = {
    "R": (1,0),
    "L": (-1,0),
    "U": (0,-1),
    "D": (0,1),
}

LENS_DIRECTIONS = {
    "/": {
        "R": "U",
        "L": "D",
        "U": "R",
        "D": "L"
    },
    "\\": {
        "R": "D",
        "L": "U",
        "U": "L",
        "D": "R"
    },
    "|": {
        "R": "UD",
        "L": "UD",
        "U": "U",
        "D": "D"
    },
    "-": {
        "R": "R",
        "L": "L",
        "U": "RL",
        "D": "RL"
    }
}

def getNextBeamPosition(beam):
    x,y,direction = beam
    vectorX, vectorY = DIRECTION_VECTORS[direction]
    newX = x + vectorX
    newY = y + vectorY
    return [newX, newY, direction]

def getInput():
    input_raw = loadFileByLine("2023/inputs/day16_data.txt")
    return input_raw

def getHash(x,y):
    return str(x) + "." + str(y)

def buildMap(input):
    height = len(input)
    width = len(input[0])
    lenses = {}

    for y in range(height):
        for x in range(width):
            lens = input[y][x]
            if lens != '.':
                lenses[getHash(x,y)] = lens
    return [width, height, lenses]

def updateVisitedNodes(visitedNodes, beams):
    for beam in beams:
        x, y, direction = beam
        hash = getHash(x, y)
        if hash not in visitedNodes:
            visitedNodes[hash] = {}
        visitedNodes[hash][direction] = True

def removeExtraBeams(visitedNodes, beams, width, height):
    def isExtraBeam(beam):
        x, y, direction = beam
        hash = getHash(x,y)
        alreadySeen = hash in visitedNodes and direction in visitedNodes[hash]
        outOfBounds = x < 0 or x >= width or y < 0 or y >= height
        if alreadySeen or outOfBounds:
            return False
        return True
    
    return list(filter(isExtraBeam, beams))


def getBeamsFromLens(beam, lens):
    x,y,direction = beam
    newDirections = LENS_DIRECTIONS[lens][direction]
    newBeams = []
    for newDirection in newDirections:
        newBeam = [x,y,newDirection]
        newBeams.append(getNextBeamPosition(newBeam))
    return newBeams

def getNextBeamPositions(beams, lenses):
    newBeams = []
    for beam in beams:
        x,y,direction = beam
        lensHash = getHash(x,y)
        if lensHash in lenses:
            newBeams.extend(getBeamsFromLens(beam, lenses[lensHash]))
        else:
            newBeams.append(getNextBeamPosition(beam))
    return newBeams

def getEnergizedCount(startingBeams, width, height, lenses):
    beams = []
    beams.extend(startingBeams)
    visitedNodes = {}
    updateVisitedNodes(visitedNodes, beams)

    while len(beams):
        beams = getNextBeamPositions(beams, lenses)
        beams = removeExtraBeams(visitedNodes, beams, width, height)
        updateVisitedNodes(visitedNodes, beams)
    
    return len(visitedNodes)
            
def getStartingBeamsList(width, height):
    startingBeamsList = []
    for x in range(width):
        startingBeamsList.append([[x,0,'D']])
        startingBeamsList.append([[x,height-1,'U']])
    for y in range(height):
        startingBeamsList.append([[0,y,'R']])
        startingBeamsList.append([[width-1,y,'L']])
    return startingBeamsList

def main():
    input = getInput()
    width, height, lenses = buildMap(input)
    print(lenses)

    startingBeamsList = getStartingBeamsList(width, height)
    energyCounts = []
    for startingBeams in startingBeamsList:
        energyCounts.append(getEnergizedCount(startingBeams, width, height, lenses))
    print(energyCounts)
    print(max(energyCounts))
main()