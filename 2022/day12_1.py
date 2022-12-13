from dijkstar import Graph, find_path
from helpers import loadFileByLine;

graph = Graph()
map_raw = loadFileByLine('inputs/day12_1.txt')
max_y = len(map_raw)
max_x = len(map_raw[0])

alphabet = 'abcdefghijklmnopqrstuvwxyz'
def getHeightValue(x,y):
    height_letter = map_raw[y][x]
    if height_letter == 'S':
        height_letter = 'a'
    if height_letter == 'E':
        height_letter = 'z'
    return alphabet.find(height_letter)

def isValidLocation(x,y):
    return x >=0 and x < max_x and y >=0 and y < max_y

def addAdjacentEdges(x, y):
    cur_height = getHeightValue(x,y)
    if isValidLocation(x-1,y) and getHeightValue(x-1,y) <= cur_height+1:
        graph.add_edge(f'{x},{y}',f'{x-1},{y}',1)
    if isValidLocation(x+1,y) and getHeightValue(x+1,y) <= cur_height+1:
        graph.add_edge(f'{x},{y}',f'{x+1},{y}',1)
    if isValidLocation(x,y-1) and getHeightValue(x,y-1) <= cur_height+1:
        graph.add_edge(f'{x},{y}',f'{x},{y-1}',1)
    if isValidLocation(x,y+1) and getHeightValue(x,y+1) <= cur_height+1:
        graph.add_edge(f'{x},{y}',f'{x},{y+1}',1)

start = {}
end = {}
for y, height_row in enumerate(map_raw):
    for x, height in enumerate(height_row):
        if height == 'S':
            start['x'] = x
            start['y'] = y
        if height == 'E':
            end['x'] = x
            end['y'] = y
        addAdjacentEdges(x,y)

print(find_path(graph, f'{start["x"]},{start["y"]}', f'{end["x"]},{end["y"]}'))
