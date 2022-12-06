import re

import colorama

from utils import *


def print_stacks(stacks):
    s = ""
    for stack in stacks:
        for container in stack:
            s += container
        s += "\n"
    print(s)


def part_one(puzzle_input: str, puzzle_input_lines: BetterList[str]):
    """
        [D]
    [N] [C]
    [Z] [M] [P]
     1   2   3

    move 1 from 2 to 1
    move 3 from 1 to 3
    move 2 from 2 to 1
    move 1 from 1 to 2
    """

    initial, movements = puzzle_input.split("\n\n")
    containers = initial.splitlines()
    column_count = int(list(filter(None, containers[-1].split()))[-1])
    containers = containers[:-1]

    pattern = re.compile("move (\d+) from (\d+) to (\d+)")
    movements = [
        [int(i) for i in pattern.match(movement).groups()]
        for movement in movements.splitlines()
    ]

    print(column_count)
    stacks = [[] for _ in range(column_count)]
    for row in containers:
        stack_index = 0
        while row:
            head = row[0:3].replace("[", "").replace("]", "")
            row = row[4:]
            if head.strip():
                stacks[stack_index] = [head] + stacks[stack_index]
            stack_index += 1

    print("initial")
    print_stacks(stacks)

    print("movements")
    for movement in movements:
        amount, _from_1_index, to_1_index = movement
        _from, to = _from_1_index - 1, to_1_index - 1
        moved = stacks[_from][-amount:]
        stacks[to] += list(reversed(moved))
        print(
            f"moving {moved}({len(moved)}/{amount}) from {_from_1_index} to {to_1_index}"
        )
        stacks[_from] = stacks[_from][:-amount]
        print_stacks(stacks)

    print_stacks(stacks)
    return "".join([i[-1] for i in stacks])


def part_two(puzzle_input: str, puzzle_input_lines: BetterList[str]):
    return None
