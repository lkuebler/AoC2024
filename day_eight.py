from utils import download_aoc_input_as_string

input_str = download_aoc_input_as_string(day=8)

# part 1
map = [[x for x in y] for y in input_str.strip().splitlines()]
antinodes = [[False for x in y] for y in map]
antennas = {}

for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j] != ".":
            if map[i][j] not in antennas.keys():
                antennas[map[i][j]] = [(i, j)]
            else:
                antennas[map[i][j]].append((i, j))
                
for key in antennas.keys():
    if len(antennas[key]) <= 1:
        continue
    for i in range(len(antennas[key])-1):
        for j in range(i+1, len(antennas[key])):
            delta_x = antennas[key][i][0] - antennas[key][j][0]
            delta_y = antennas[key][i][1] - antennas[key][j][1]
            up_pos_x = antennas[key][i][0] + delta_x
            up_pos_y = antennas[key][i][1] + delta_y
            down_pos_x = antennas[key][j][0] - delta_x
            down_pos_y = antennas[key][j][1] - delta_y
            if up_pos_x >= 0 and up_pos_x < len(map) and up_pos_y >= 0 and up_pos_y < len(map[0]):
                antinodes[up_pos_x][up_pos_y] = True
            if down_pos_x >= 0 and down_pos_x < len(map) and down_pos_y >= 0 and down_pos_y < len(map[0]):
                antinodes[down_pos_x][down_pos_y] = True
            
print(f"part 1: {sum([x.count(True) for x in antinodes])}")

# part 2
antinodes = [[False for x in y] for y in map]

for key in antennas.keys():
    if len(antennas[key]) <= 1:
        continue
    for i in range(len(antennas[key])-1):
        for j in range(i+1, len(antennas[key])):
            delta_x = antennas[key][i][0] - antennas[key][j][0]
            delta_y = antennas[key][i][1] - antennas[key][j][1]
            up_pos_x = antennas[key][i][0]
            up_pos_y = antennas[key][i][1]
            down_pos_x = antennas[key][j][0]
            down_pos_y = antennas[key][j][1]
            while up_pos_x >= 0 and up_pos_x < len(map) and up_pos_y >= 0 and up_pos_y < len(map[0]):
                antinodes[up_pos_x][up_pos_y] = True
                up_pos_x += delta_x
                up_pos_y += delta_y
            while down_pos_x >= 0 and down_pos_x < len(map) and down_pos_y >= 0 and down_pos_y < len(map[0]):
                antinodes[down_pos_x][down_pos_y] = True
                down_pos_x -= delta_x
                down_pos_y -= delta_y
                
print(f"part 2: {sum([x.count(True) for x in antinodes])}")
            