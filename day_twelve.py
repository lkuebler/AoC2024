from utils import download_aoc_input_as_string

input_str = download_aoc_input_as_string(day=12)

# part 1

map = [[x for x in y] for y in input_str.strip().splitlines()]

areas = []
visited = [[False for x in y] for y in map]

while not all([all(x) for x in visited]):
    for i in range(len(map)):
        for j in range(len(map[i])):
            if not visited[i][j]:
                stack = [(i, j)]
                visited[i][j] = True
                area = []
                while stack:
                    x, y = stack.pop()
                    area.append((x, y))
                    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                        new_x = x + dx
                        new_y = y + dy
                        if new_x >= 0 and new_x < len(map) and new_y >= 0 and new_y < len(map[0]) and map[new_x][new_y] == map[x][y] and not visited[new_x][new_y]:
                            stack.append((new_x, new_y))
                            visited[new_x][new_y] = True
                areas.append(area)
            

def perimeter(area):
    all_neighbours = set()
    for x, y in area:
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_x = x + dx
            new_y = y + dy
            if (new_x, new_y) not in area:
                all_neighbours.add((new_x, new_y, dx, dy))
    return len(all_neighbours)
    
 
res = 0
for area in areas:
    print(f"adding {len(area)} * {perimeter(area)}")
    res += len(area) * perimeter(area)
    
print(f"part 1: {res}")

# part 2

def number_of_sides(area):
    all_neighbours = set()
    for x, y in area:
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_x = x + dx
            new_y = y + dy
            if (new_x, new_y) not in area:
                all_neighbours.add((new_x, new_y, dx, dy))
                
    horizontal = [(1, 0), (-1, 0)]
    vertical = [(0, 1), (0, -1)]
    count = 0
    visited = set()
    for x, y, dx, dy in all_neighbours:
        if (x, y, dx, dy) in visited:
            continue
        visited.add((x, y, dx, dy))
        count += 1
        stack = [(x, y)]
        new_dirs = horizontal if dx == 0 else vertical
        while stack:
            x, y = stack.pop()
            for dir_x, dir_y in new_dirs:
                new_x = x + dir_x
                new_y = y + dir_y
                if (new_x, new_y, dx, dy) in all_neighbours and (new_x, new_y, dx, dy) not in visited:
                    visited.add((new_x, new_y, dx, dy))
                    stack.append((new_x, new_y))
    return count
        

res = 0
for area in areas:
    print(f"adding {len(area)} * {number_of_sides(area)}")
    res += len(area) * number_of_sides(area)
    
print(f"part 2: {res}")