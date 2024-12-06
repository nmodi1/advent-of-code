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


def solution(report_list: list[list[int]], p2_enabled: bool = True) -> int:
    num_safe = 0
    for report in report_list:
        if check_safe(report):
            num_safe += 1

        elif p2_enabled:
            # Brute force it
            for i in range(len(report)):
                copy = report.copy()
                copy.pop(i)
                if check_safe(copy):
                    num_safe += 1
                    break

    return num_safe


# Test
report_list = parse_input(TEST_INPUT_PATH)
print(
    f"Test - Part1 = {solution(report_list, False)} | Part2 = {solution(report_list, True)}"
)
print()

# Actual
report_list = parse_input(INPUT_PATH)
print(
    f"Actual - Part1 = {solution(report_list, False)} | Part2 = {solution(report_list, True)}"
)
