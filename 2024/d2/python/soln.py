import os

from input import read_input

cwd = os.getcwd()
INPUT_PATH = f"{cwd}/2024/d2/input.txt"
TEST_INPUT_PATH = f"{cwd}/2024/d2/input-test.txt"


def parse_input(input_path: str) -> list[list[int]]:
    file_lines = read_input(input_path, True)

    input_list = []
    for line in file_lines:
        input_list.append([int(num) for num in line.split()])

    return input_list


# Check all are gradually changing and within accepted range
def check_safe(report: list[int]) -> bool:
    if report[0] < report[1]:
        # Increasing
        return all(1 <= curr - prev <= 3 for prev, curr in zip(report, report[1:]))
    else:
        # Decreasing
        return all(1 <= prev - curr <= 3 for prev, curr in zip(report, report[1:]))


def solution(report_list: list[list[int]]) -> int:
    num_safe = 0
    for report in report_list:
        num_safe += 1 if check_safe(report) else 0

    return num_safe


report_list = parse_input(INPUT_PATH)
# print(report_list)
ans = solution(report_list)
print(ans)
