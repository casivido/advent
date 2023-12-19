from shapely.geometry import Polygon
from helpers import loadFileByLine

import pprint
print = pprint.PrettyPrinter(indent=2).pprint

HEX_DIRECTION_MAP = "RDLU"

def getInstructions():
    instructions_raw = loadFileByLine("2023/inputs/day18_data.txt")
    hexInstructions = list(map(lambda line: line.split(" ")[2], instructions_raw))
    decryptedInstructions = []
    for hex in hexInstructions:
        hexMagnitude = hex[2:-2]
        magnitude = int(hexMagnitude, 16)
        hexDirection = int(hex[-2])
        direction = HEX_DIRECTION_MAP[hexDirection]
        decryptedInstructions.append((direction, magnitude))
    return decryptedInstructions

def getNextCoordinate(oldCoordinate, instructionLine):
    newX, newY = oldCoordinate
    direction, magnitude = instructionLine
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
    print(poly.area)
main()