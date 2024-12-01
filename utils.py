import os
import requests

def download_aoc_input_as_string(day: int) -> str:
    url = f"https://adventofcode.com/2024/day/{day}/input"
    cookie = os.getenv("AOC_SESSION_COOKIE")
    if not cookie:
        raise ValueError("Missing AOC_SESSION_COOKIE environment variable")
    headers = {"cookie": f"session={cookie}"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.text