import re

import colorama

from utils import *


def transpose(l, true_to_pad_back_false_to_pad_front=True):
    depth = max([len(ll) for ll in l])
    new_grid = []
    # print(f"{depth=}")
    # print(f"{l=}")
    for ll in l:
        new_list = ll[:]
        # print(f"{ll=}")
        while len(new_list) < depth:
            if true_to_pad_back_false_to_pad_front:
                new_list.append(
                    "___"
                )  # the row is a slice of columns so we need to have each row be the same length
                # print(f"{new_list=}")
            else:  # the row IS the column in the case because we have it transposed
                new_list = ["___"] + new_list
        new_grid.append(new_list)
    # print(new_grid)
    return list([list(_) for _ in zip(*new_grid)])


file_opened = False


def print_rows(l, col_nums=True, prepend=None, movement=None, amount=None):
    symbols = {}
    if movement:
        from_, to_ = movement
        symbols = {from_: "^", to_: "v"}
    buffer = (
        " " + str("".join([f" {i+1} " for i in range(len(l[0]))])) if col_nums else ""
    )
    movement_buffer = (
        " "
        + str(
            "".join(
                [f" {symbols[i]} " if i in symbols else "   " for i in range(len(l[0]))]
            )
        )
        if col_nums
        else ""
    )
    movement_num_buffer = (
        " "
        + str(
            "".join(
                [f"{amount: 2d} " if i in symbols else "   " for i in range(len(l[0]))]
            )
        )
        if col_nums
        else ""
    )
    s = ""
    # if movement:
    #     for rid, row in enumerate(l):
    #         s += " "
    #         for cid, col in enumerate(row):
    #             if cid == from_:
    #                 s += colorama.Fore.LIGHTRED_EX + col + colorama.Fore.RESET
    #             if cid == to_:
    #                 s += colorama.Fore.LIGHTGREEN_EX + col + colorama.Fore.RESET
    #             else:
    #                 s += col
    #         s += "\n"
    #     cols = s  # "".join(list(f" {''.join(ll)}\n" for i, ll in enumerate(l)))
    # else:
    cols = "".join(
        list(f"{(len(l) - li):3d} {''.join(ll)}\n" for li, ll in enumerate(l))
    )
    print(
        f"ROWS{'(' + prepend + ')' if prepend else ''}: \n"
        + "   "
        + movement_num_buffer
        + "\n"
        + "   "
        + ((movement_buffer + "\n") if amount else "")
        + cols
        + "   "
        + buffer
    )


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

    stack, movements = puzzle_input.split("\n\n")
    stack_lines = stack.splitlines()
    columns = [int(s.strip()) for s in stack_lines[-1].split()]
    column_count = columns[-1]

    new_rows = []
    for row in stack_lines[:-1]:
        new_row = []
        for _ in range(column_count):
            container = row[0:4]
            row = row[4:].lstrip()
            new_row.append(container.strip() if container.strip() else "___")
        new_rows.append(new_row)
    new_rows = transpose(new_rows)

    print("starting movements")

    for mov_index, movement in enumerate(movements.splitlines()):
        move_num, source, target = re.match(
            "move (\d+) from (\d+) to (\d+)", movement
        ).groups()
        move_num, source, target = int(move_num), int(source) - 1, int(target) - 1
        # print(f"move {move_num} from {source+1} to {target + 1}")
        print_rows(
            new_rows,
            movement=(source, target),
            amount=move_num,
            prepend="initial" if not mov_index else None,
        )
        move = ""
        for _ in range(move_num):
            # print(f"moving {_ + 1} of {move_num}")
            # print(f"{new_rows[source]=}")
            # print(f"{new_rows[target]=}")

            head = "___"
            while len(new_rows[source]) and head == "___":
                head, *n = new_rows[source]
                new_rows[source] = n
            if not head or head == "___":
                continue
            # print(f"{head=} {n=}")
            new_rows[source] = n
            if len(new_rows[target]):
                target_head = new_rows[target][0]
                while len(new_rows[target]) and target_head == "___":
                    target_head, *target_n = new_rows[target]
                    new_rows[target] = target_n
            assert head and head != "___", f"{head=}"
            new_rows[target] = [head] + new_rows[target]
            move += str(head).replace("[", "").replace("]", "").replace("_", "")
            # print(f"{new_rows[source]=}")
            # print(f"{new_rows[target]=}")
        # print_rows(
        #     transpose(new_rows, False), movement=(source, target), amount=move_num
        # )
        print(
            f"    moved {move} ({len(move)}/{move_num}) from {source+1} to {target+1}"
        )
    s = ""
    for row in new_rows:
        if len(row):
            s += row[0].replace("[", "").replace("]", "").replace("_", "")
    print_rows(new_rows)
    print(f"FINAL:\n{s}")
    return s


def part_two(puzzle_input: str, puzzle_input_lines: BetterList[str]):
    return None
