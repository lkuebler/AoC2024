from utils import download_aoc_input_as_string
from tqdm import tqdm

input_str = download_aoc_input_as_string(day=7)

# part 1

def get_operators(length):
    if length == 1:
        return [["+"], ["*"]]
    else:
        res = []
        operators_list = get_operators(length - 1)
        for operators in operators_list:
            res.append(operators + ["+"])
            res.append(operators + ["*"])
        return res

def calculate_left_to_right(operands, operators):
    res = operands[0]
    for i in range(len(operators)):
        if operators[i] == "+":
            res += operands[i + 1]
        else:
            res *= operands[i + 1]
    return res

total_sum = 0
for line in input_str.strip().splitlines():
    res = int(line.split(":")[0])
    operands = list(map(int, line.split(":")[1].strip().split(" ")))
    operators_list = get_operators(len(operands) - 1)
    results = list(map(lambda operators: calculate_left_to_right(operands.copy(), operators.copy()), operators_list))
    if res in results:
        total_sum += res
print(f"part 1: {total_sum}")

def get_extended_operators(length):
    if length == 1:
        return [["+"], ["*"], ["||"]]
    else:
        res = []
        operators_list = get_extended_operators(length - 1)
        for operators in operators_list:
            res.append(operators + ["+"])
            res.append(operators + ["*"])
            res.append(operators + ["||"])
        return res
    
def calculate_part_two(operands, operators, max):
    res = operands[0]
    for i in range(len(operators)):
        if res > max:
            return -1
        if operators[i] == "||":
            res = int(str(res) + str(operands[i + 1]))
        elif operators[i] == "+":
            res += operands[i + 1]
        else:
            res *= operands[i + 1]
    return res

total_sum = 0
for line in tqdm(input_str.strip().splitlines()):
    res = int(line.split(":")[0])
    operands = list(map(int, line.split(":")[1].strip().split(" ")))
    operators_list = get_extended_operators(len(operands) - 1)
    results = list(map(lambda operators: calculate_part_two(operands.copy(), operators.copy(), res+1), operators_list))
    if res in results:
        total_sum += res
        
print(f"part 2: {total_sum}")