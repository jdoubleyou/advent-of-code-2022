import re

import colorama

from utils import *


def transpose(
    l,
    outer_lists_are_stack_cross_sections=True,
    transpose_top_of_stack_to_end_of_list=True,
):
    depth = max([len(ll) for ll in l])
    new_grid = []
    # print(f"{depth=}")
    # print(f"{l=}")
    for ll in l:
        new_list = ll[:]
        # print(f"{ll=}")
        while len(new_list) < depth:
            if outer_lists_are_stack_cross_sections:
                new_list.append(
                    "___"
                )  # the row is a slice of columns so we need to have each row be the same length
                # print(f"{new_list=}")
            else:  # the row IS the column in the case because we have it transposed
                new_list = ["___"] + new_list
        new_grid.append(new_list)
    if transpose_top_of_stack_to_end_of_list:
        return list([list(reversed(_)) for _ in zip(*new_grid)])
    else:
        return list([list(_) for _ in zip(*new_grid)])


def print_rows(l, col_nums=True, prepend=None, movement=None, amount=None):
    symbols = {}
    depth = max([len(ll) for ll in l])
    depth_plus_space = depth + 5
    from_ = None
    to_ = None
    if movement:
        from_, to_ = movement
        symbols = {from_: "<", to_: ">"}
    indent = "         "
    buffer = (
        str("".join([f"{i+1:3d}" for i in range(depth_plus_space)])) if col_nums else ""
    )
    buffer = indent + buffer + "\n"

    def thing(show_moved, ll):
        new_ll = []
        if show_moved and amount:
            not_moved = ll[: (-1 * amount)]
            moved = ll[len(ll) - amount :]
        else:
            not_moved = ll
            moved = []
        for lll in not_moved:
            new_ll.append(lll)
        for lll in moved:
            new_ll.append(lll.replace("[", "<").replace("]", ">"))
        padded = new_ll + [" . " for _ in range(0, depth_plus_space - len(ll))]
        return "".join(padded)

    cols = "".join(
        list(
            (f"{amount: 4d} {symbols[li]}" if li in symbols else "      ")
            + f"{(li + 1):3d}|{thing(li==from_, ll)}\n"
            for li, ll in enumerate(l)
        )
    )
    line = "+" * ((depth_plus_space * 3) + 9)
    line = indent + line + "\n"
    print(
        f"ROWS{'(' + prepend + ')' if prepend else ''}: \n"
        + line
        + cols
        + buffer
        + line
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
    new_rows = [[col for col in row if col != "___"] for row in new_rows]
    print_rows(new_rows, prepend="initial")

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
            prepend="starting movements" if not mov_index else None,
        )
        move = ""
        for _ in range(move_num):
            # print(f"moving {_ + 1} of {move_num}")
            # print(f"{new_rows[source]=}")
            # print(f"{new_rows[target]=}")

            head = "___"
            while len(new_rows[source]) and head == "___":
                head = new_rows[source][-1]
                new_rows[source] = new_rows[source][:-1]
            if not head or head == "___":
                continue
            # print(f"{head=} {n=}")
            if len(new_rows[target]):
                target_head = new_rows[target][-1]
                while len(new_rows[target]) and target_head == "___":
                    target_head, *target_n = new_rows[target]
                    new_rows[target] = target_n
            assert head and head != "___", f"{head=}"
            new_rows[target] += [head]
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
            s += row[-1].replace("[", "").replace("]", "").replace("_", "")
    print_rows(new_rows)
    print(f"FINAL:\n{s}")
    return s


def part_two(puzzle_input: str, puzzle_input_lines: BetterList[str]):
    return None
