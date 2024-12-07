from utils import download_aoc_input_as_string

input_str = download_aoc_input_as_string(day=4)
# part 1
letters = [[char for char in line] for line in input_str.split("\n") if line]
word = "XMAS"
directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

def recursive_search(i, j, searched_char, d_i, d_j):
    if i < 0 or i >= len(letters) or j < 0 or j >= len(letters[i]):
        return 0
    if letters[i][j] != searched_char:
        return 0
    if searched_char == "S":
        return 1
    return recursive_search(i + d_i, j + d_j, word[word.index(searched_char) + 1], d_i, d_j)

count_xmas = sum(sum(sum(recursive_search(i, j, "X", dir[0], dir[1]) for dir in directions) for j in range(len(letters[i])) if letters[i][j] == "X") for i in range(len(letters)))
print(f"part 1: {count_xmas}")

# part 2
def isdiagMas(diag):
    return "M" in diag and "S" in diag

def isXmas(i, j):
    return letters[i][j] == "A" and isdiagMas({letters[i+1][j+1], letters[i-1][j-1]}) and isdiagMas({letters[i-1][j+1], letters[i+1][j-1]})

count_Xmas = sum(sum(isXmas(i, j) for j in range(1, len(letters[i])-1)) for i in range(1, len(letters)-1))
print(f"part 2: {count_Xmas}")