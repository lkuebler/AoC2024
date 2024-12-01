from utils import download_aoc_input_as_string

input_str = download_aoc_input_as_string(day=1)

# part 1
first, second = zip(*map(lambda x: (int(x.split("   ")[0]), int(x.split("   ")[1])), input_str.strip().splitlines()))

first = sorted(first)
second = sorted(second)

abs_dist = sum(map(lambda x: abs(x[0] - x[1]), zip(first, second)))

print(f"part 1: {abs_dist}")

# part 2
similarity_sum = 0

for elem in first:
    occurences = len(list(filter(lambda x: x == elem, second)))
    similarity_sum += elem * occurences
    
print(f"part 2: {similarity_sum}")