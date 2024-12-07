from utils import download_aoc_input_as_string
import re

input_str = download_aoc_input_as_string(day=3)

# part 1
regex = r"mul\((\d{1,3}),(\d{1,3})\)"
matches = re.findall(regex, input_str)
sum = 0
for match in matches:
    sum += int(match[0]) * int(match[1])
print(f"part 1: {sum}")

#part 2
do_pattern = r"do\(\)"
dont_pattern = r"don't\(\)"
indexed_matches = list(re.finditer(regex, input_str))
indexed_matches = [(match.start(), int(match.group(1)) * int(match.group(2))) for match in indexed_matches]

indexed_do = list(re.finditer(do_pattern, input_str))
indexed_dont = list(re.finditer(dont_pattern, input_str))
indexed_do = [(match.start(), True) for match in indexed_do]
indexed_dont = [(match.start(), False) for match in indexed_dont]
combined = indexed_matches + indexed_do + indexed_dont
combined.sort(key=lambda x: x[0])

enabled = True
sum = 0
for i in range(len(combined)):
    if combined[i][1] == True:
        enabled = True
    elif combined[i][1] == False:
        enabled = False
    else:
        if enabled:
            sum += combined[i][1]

print(f"part 2: {sum}")

