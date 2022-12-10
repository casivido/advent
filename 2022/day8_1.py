from helpers import loadFileByLine;

forest_heights = loadFileByLine("inputs/day8_1.txt")

forest_dimensions = {
    "x": len(forest_heights[0]),
    "y": len(forest_heights)
}

visible_tree_locations = {}

directions = {
    "from_top": {
        "view_axis": "y",
        "other_axis": "x",
        "start": 0,
        "end": forest_dimensions["y"],
        "increment": 1
    },
    "from_bottom": {
        "view_axis": "y",
        "other_axis": "x",
        "start": forest_dimensions["y"]-1,
        "end": -1,
        "increment": -1
    },
    "from_left": {
        "view_axis": "x",
        "other_axis": "y",
        "start": 0,
        "end": forest_dimensions["x"],
        "increment": 1
    },
    "from_right": {
        "view_axis": "x",
        "other_axis": "y",
        "start": forest_dimensions["x"]-1,
        "end": -1,
        "increment": -1
    }
}

for direction_data in directions.values():
    cur_location = {
        "x": 0,
        "y": 0
    }
    view_axis = direction_data["view_axis"]
    other_axis = direction_data["other_axis"]

    while cur_location[other_axis] < forest_dimensions[other_axis]:
        previous_max_height = -1
        cur_location[view_axis] = direction_data["start"]
        while cur_location[view_axis] != direction_data["end"]:
            cur_tree_height = int(forest_heights[cur_location["y"]][cur_location["x"]])
            if cur_tree_height > previous_max_height:
                previous_max_height = cur_tree_height
                visible_tree_locations[f"{cur_location['x']},{cur_location['y']}"] = True
            cur_location[view_axis] += direction_data['increment']
        cur_location[other_axis] += 1

print(len(visible_tree_locations))