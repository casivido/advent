from shapely.geometry import Polygon
from helpers import loadFileByLine

import pprint
print = pprint.PrettyPrinter(indent=2).pprint

def getInstructions():
    instructions_raw = loadFileByLine("2023/inputs/day18_data.txt")
    return list(map(lambda line: line.split(" "), instructions_raw))

def getNextCoordinate(oldCoordinate, instructionLine):
    newX, newY = oldCoordinate
    direction, magnitude, color = instructionLine
    match direction:
        case "R":
            newX += int(magnitude)
        case "L":
            newX -= int(magnitude)
        case "U":
            newY -= int(magnitude)
        case "D":
            newY += int(magnitude)
    return (newX,newY)
            
def main():
    instructions = getInstructions()
    coordinates = [[0,0]]
    for instructionLine in instructions:
        coordinates.append(getNextCoordinate(coordinates[-1], instructionLine))
    poly = Polygon(coordinates).buffer(.5, cap_style="square", join_style="mitre")
    print(coordinates)
    print(poly.area)
main()