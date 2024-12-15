from utils import download_aoc_input_as_string

input_str = download_aoc_input_as_string(day=15)

# part 1
original_map = []
directions = []
for line in input_str.strip().splitlines():
    if "#" in line:
        original_map.append([x for x in line])
    else:
       directions += [x for x in line.removesuffix("\n")]
map = [x.copy() for x in original_map]

def get_robot_location(map):
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == "@":
                return i, j
    return -1, -1

def get_direction(direction):
    if direction == ">":
        return 0, 1
    elif direction == "<":
        return 0, -1
    elif direction == "^":
        return -1, 0
    elif direction == "v":
        return 1, 0
    else:
        return 0, 0

def move_robot_one_step(map, direction):
    # print(f"moving robot in direction {direction}")
    # for line in map:
    #     print("".join(line))
    # print("-------------------------------------------------")
    x, y = get_robot_location(map)
    x_dir, y_dir = get_direction(direction)
    x_new, y_new = x + x_dir, y + y_dir
    if map[x_new][y_new] == "#":
        return
    while (map[x_new][y_new] == "O"):
        x_new, y_new = x_new + x_dir, y_new + y_dir
    if map[x_new][y_new] == "#":
            return
    map[x][y] = "."
    map[x_new][y_new] = "O"
    map[x + x_dir][y + y_dir] = "@"
    return

for direction in directions:
    move_robot_one_step(map, direction)

def get_score(map):
    score = 0
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == "O" or map[i][j] == "[":
                score += 100 * i + j
    return score

print(f"part 1: {get_score(map)}")

# part 2
mappings = {"#": "##", "O": "[]", ".": "..", "@": "@."}
new_map = []
for line in original_map:
    new_line = []
    for x in line:
        new_line.append(mappings[x][0])
        new_line.append(mappings[x][1])
    new_map.append(new_line)

class COORDINATE:
    x: int
    y: int
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

def is_able_to_move(map, location, direction, coords_to_change) -> bool:
    coords_to_change.add(location)
    new_location = COORDINATE(location.x + direction.x, location.y + direction.y)
    if map[new_location.x][new_location.y] == "#":
        return False
    if map[new_location.x][new_location.y] == ".":
        return True
    if direction.x == 0:
        return is_able_to_move(map, new_location, direction, coords_to_change)
    y_change_second = 1 if map[new_location.x][new_location.y] == "[" else -1
    second = COORDINATE(new_location.x, new_location.y + y_change_second)
    return is_able_to_move(map, new_location, direction, coords_to_change) and is_able_to_move(map, second, direction, coords_to_change)

def complex_robot_move(map, direction):
    # print(f"moving robot in direction {direction}")
    # for line in map:
    #     print("".join(line))
    # print("-------------------------------------------------")
    
    x, y = get_robot_location(map)
    x_dir, y_dir = get_direction(direction)
    location = COORDINATE(x, y)
    direction = COORDINATE(x_dir, y_dir)
    coords_to_change = set()
    if is_able_to_move(map, location, direction, coords_to_change):
        new_map = [[x for x in y] for y in map]
        for coord in coords_to_change:
            new_map[coord.x][coord.y] = "."
        for coord in coords_to_change:
            new_map[coord.x + x_dir][coord.y + y_dir] = map[coord.x][coord.y]
        return new_map
    return map

for direction in directions:
    new_map = complex_robot_move(new_map, direction)
    
print(f"part 2: {get_score(new_map)}")