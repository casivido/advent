
from helpers import loadFileByLine
from dijkstar import Graph, find_path
graph = Graph()
# >>> graph.add_edge(1, 2, 110)
# >>> graph.add_edge(2, 3, 125)
# >>> graph.add_edge(3, 4, 108)
# >>> find_path(graph, 1, 4)

DIRECTIONS = ["Up", "Down", "Left", "Right"]
DIRECTION_OPPOSITES = {
    "Up": "Down",
    "Left": "Right",
    "Down": "Up",
    "Right": "Left"
}
MAX_MOMENTUM = 3

map = loadFileByLine("2023/inputs/day17_data.txt")
height = len(map)
width = len(map[0])

def getNodeName(x, y, direction = None, momentum = None):
    isFinalNode = (x == (width - 1)) and (y == (height - 1))
    if isFinalNode:
        return str(x) + '.' + str(y) + ' FINAL'
    return str(x) + '.' + str(y) + ' ' + direction + '(' + str(momentum) + ')'

def isNodeInBounds(node):
    return (0 <= node[0] <= width - 1) and (0 <= node[1] <= height - 1)

def getEdgesToNode(x, y, weight):
    edgesToAdd = []
    nodesToCheck = [ # Directions are opposite due to the inverse setting of edges
        (x+1,y,'Left'),
        (x-1,y,'Right'),
        (x,y+1,'Up'),
        (x,y-1,'Down')
    ]
    adjacentNodes = list(filter(isNodeInBounds, nodesToCheck))
    for (adjX,adjY,momentumDirection) in adjacentNodes:
        adjNodeStates = getAllNodeStates((adjX,adjY))
        for (stateX, stateY, stateDirection, stateMomentum) in adjNodeStates:
            # Can't turn around
            if DIRECTION_OPPOSITES[stateDirection] == momentumDirection:
                continue
            momentum = 1
            if stateDirection == momentumDirection:
                momentum = stateMomentum + 1
                if momentum > 3:
                    continue
            edgesToAdd.append([getNodeName(stateX,stateY,stateDirection,stateMomentum), getNodeName(x,y,momentumDirection,momentum), weight])
    return edgesToAdd
                
def getAllNodeStates(node):
    x = node[0]
    y = node[1]
    states = []
    for momentum in range(1,MAX_MOMENTUM+1):
        for direction in DIRECTIONS:
            states.append([x,y,direction,momentum])
    return states

for y in range(height):
    for x in range(width):
        weight = int(map[y][x])
        
        for (fromEdge, toEdge, weight) in getEdgesToNode(x,y,weight):
            graph.add_edge(fromEdge, toEdge, weight)

startingNodeName = getNodeName(0, 0, "Down", 1)
endNodeName = getNodeName(width-1,height-1)

print(find_path(graph, startingNodeName, endNodeName))