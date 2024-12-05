import os

cwd = os.getcwd()
INPUT_PATH = f"{cwd}/2024/d1/inputs/input.txt"
TEST_INPUT_PATH = f"{cwd}/2024/d1/inputs/test.txt"


# Parse input and return 2 lists
def parse_input(input_path: str) -> tuple[list[str], list[str]]:
    list1, list2 = [], []
    with open(input_path, "r") as f:
        for line in f.readlines():
            if len(line.rstrip()) > 0:
                num1, num2 = map(int, line.split())
                list1.append(num1)
                list2.append(num2)

    return list1, list2


# Return total distance between the lists
def solution(l1: list[str], l2: list[str]) -> int:
    l1.sort()
    l2.sort()

    dist = 0
    for i, j in zip(l1, l2):
        dist += abs(i - j)

    return dist


# Test
test = solution(*parse_input(TEST_INPUT_PATH))

# Actual
result = solution(*parse_input(INPUT_PATH))

print(f"Test = {test}")
print(f"Actual = {result}")
