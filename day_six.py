from utils import download_aoc_input_as_string
from tqdm import tqdm

input_str = download_aoc_input_as_string(day=6)

# part 1

map = [[x for x in y] for y in input_str.strip().splitlines()]
original_map = [[x for x in y] for y in input_str.strip().splitlines()]
directions = [">", "v", "<", "^"]

def get_guard_pos(map):
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] in directions:
                return i, j
    return -1, -1

def get_next_pos(pos, direction):
    i, j = pos
    if direction == ">":
        return i, j + 1
    if direction == "v":
        return i + 1, j
    if direction == "<":
        return i, j - 1
    if direction == "^":
        return i - 1, j
    
def turn_right(direction):
    return directions[(directions.index(direction) + 1) % 4]
    
def one_iteration(map):
    x_cur, y_cur = get_guard_pos(map)
    if x_cur == -1:
        return -1 # is this needed really??
    x_next, y_next = get_next_pos((x_cur, y_cur), map[x_cur][y_cur])
    if x_next < 0 or y_next < 0 or x_next >= len(map) or y_next >= len(map[x_next]):
        return -1
    if map[x_next][y_next] in [".", "X"]:
        map[x_next][y_next] = map[x_cur][y_cur]
        map[x_cur][y_cur] = "X"  
        return 1  
    elif map[x_next][y_next] == "#":
        new_direction = turn_right(map[x_cur][y_cur])
        map[x_cur][y_cur] = new_direction
        return 0
    return -1
    
while one_iteration(map):
    pass

print(f"part 1: {sum([x.count("X") for x in map]) + 1}")

# part 2

# no time.....