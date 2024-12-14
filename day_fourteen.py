from utils import download_aoc_input_as_string
from tqdm import tqdm

input_str = download_aoc_input_as_string(day=14)

# part 1
class COORDINATE:
    x: int
    y: int
    
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

class ROBOT:
    pos: COORDINATE
    vel: COORDINATE
    
    def __init__(self, x, y, vx, vy):
        self.pos = COORDINATE(x, y)
        self.vel = COORDINATE(vx, vy)
        
def get_robots(input_string):
    robots = []
    for line in input_string.strip().splitlines():
        pos = line.split(" ")[0].split("=")[1]
        vel = line.split(" ")[1].split("=")[1]
        x = int(pos.split(",")[0])
        y = int(pos.split(",")[1])
        vx = int(vel.split(",")[0])
        vy = int(vel.split(",")[1])
        robots.append(ROBOT(x, y, vx, vy))
    return robots

robots = get_robots(input_str)
WIDTH = 101
HEIGHT = 103

def move_robot(robot):
    robot.pos.x = (robot.pos.x + robot.vel.x) % WIDTH
    robot.pos.y = (robot.pos.y + robot.vel.y) % HEIGHT
    
def move_robots(robots):
    for robot in robots:
        move_robot(robot)

for i in range(100):
    move_robots(robots)
    
def get_score(robots):
    first_quadrant_score = 0
    second_quadrant_score = 0
    third_quadrant_score = 0
    fourth_quadrant_score = 0
    for robot in robots:
        if robot.pos.x < WIDTH // 2 and robot.pos.y < HEIGHT // 2:
            first_quadrant_score += 1
        elif robot.pos.x > WIDTH // 2 and robot.pos.y < HEIGHT // 2:
            second_quadrant_score += 1
        elif robot.pos.x > WIDTH // 2 and robot.pos.y > HEIGHT // 2:
            third_quadrant_score += 1
        elif robot.pos.x < WIDTH // 2 and robot.pos.y > HEIGHT // 2:
            fourth_quadrant_score += 1
    return first_quadrant_score * second_quadrant_score * third_quadrant_score * fourth_quadrant_score



print(f"part 1: {get_score(robots)}")
    
    
# part 2
def print_map(robots):
    robot_map = [[0 for _ in range(HEIGHT)] for _ in range(WIDTH)]
    for robot in robots:
        robot_map[robot.pos.x][robot.pos.y] = 1
    robot_map = [[" " if x == 0 else "#" for x in row] for row in robot_map]
    for row in robot_map:
        print("".join([str(x) for x in row]))

robots = get_robots(input_str)
num_of_robots = len(robots)

def biggest_neighbouring_area(robots):
    robot_map = [[0 for _ in range(HEIGHT)] for _ in range(WIDTH)]
    for robot in robots:
        robot_map[robot.pos.x][robot.pos.y] = 1
    visited = [[False for _ in range(HEIGHT)] for _ in range(WIDTH)]
    max_area = 0
    for i in range(WIDTH):
        for j in range(HEIGHT):
            if robot_map[i][j] == 1 and not visited[i][j]:
                stack = [(i, j)]
                visited[i][j] = True
                area = 1
                while stack:
                    x, y = stack.pop()
                    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                        new_x = x + dx
                        new_y = y + dy
                        if new_x >= 0 and new_x < WIDTH and new_y >= 0 and new_y < HEIGHT and robot_map[new_x][new_y] == 1 and not visited[new_x][new_y]:
                            stack.append((new_x, new_y))
                            visited[new_x][new_y] = True
                            area += 1
                max_area = max(max_area, area)
    return max_area

for i in tqdm(range(1000000)):
    if (area_size := biggest_neighbouring_area(robots)) > 0.1 * num_of_robots:
        print_map(robots)
        print((f"iteration: {i}  with area size {area_size} " + "- " * 50)[:103])
        input()
    move_robots(robots)