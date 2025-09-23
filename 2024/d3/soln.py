import os
import re

cwd = os.getcwd()
INPUT_PATH = f"{cwd}/2024/d3/input-d3.txt"
TEST_INPUT_PATH = f"{cwd}/2024/d3/input-test-d3.txt"

instruction_regex = r"(mul\(\d+,\d+\))"

p2_regex = r"(mul\(\d+,\d+\))|do\(\)|don't\(\)"

num_regex = r"(\d+,\d+)"

def p1(content:str):
    instructions = re.findall(instruction_regex, content)


    result = 0
    for instruction in instructions:
        nums = re.search(num_regex, instruction)[0].split(",")
        result += int(nums[0]) * int(nums[1])
    
    return result

def p2(content:str):
    instructions = re.findall(p2_regex, content)
    print(content)
    print(instructions)

    result = 0
    skip = False
    for instruction in instructions:
        print (instruction)
        if skip:
            print("SKIP")
            continue
        print("NO SKIP")
        
        if "mul" in instruction:
            nums = re.search(num_regex, instruction)[0].split(",")
            result += int(nums[0]) * int(nums[1])
        else:
            skip = (instruction == "don't()")

    return result




with open(TEST_INPUT_PATH) as file:
    content = file.read()


instructions = re.findall(p2_regex, content)
print(content, end="\n\n")
print(instructions)

# result = p2(content)

# print(result)