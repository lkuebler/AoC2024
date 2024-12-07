from utils import download_aoc_input_as_string
from tqdm import tqdm

input_str = download_aoc_input_as_string(day=2)
# part 1 & 2
def is_safe_report(arr):
    if sorted(arr) == arr or sorted(arr, reverse=True) == arr:
        safe_diffs = True
        arr = sorted(arr, reverse=True)
        for i in range(len(arr) - 1):
            diff = arr[i] - arr[i + 1]
            if diff < 1 or diff > 3:
                safe_diffs = False
        return safe_diffs


safe_report_count = 0
safe_report_with_deletion_count = 0

for line in tqdm(input_str.splitlines()):
    arr = list(map(int, line.split(" ")))
    if is_safe_report(arr):
        safe_report_count += 1
    else:
        for j in range(len(arr)):
            if is_safe_report(arr[:j] + arr[j + 1:]):
                safe_report_with_deletion_count += 1
                break

print(f"part 1: {safe_report_count}")
print(f"part 2: {safe_report_count + safe_report_with_deletion_count}")
