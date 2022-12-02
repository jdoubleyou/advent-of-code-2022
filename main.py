import argparse
from importlib import import_module
from pathlib import Path

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("day", type=int, choices=tuple(range(1, 26)))
    parser.add_argument("part", type=int, choices=(1, 2))
    parser.add_argument("--example", action="store_true")
    parser.add_argument("--prompt", action="store_true")
    args = parser.parse_args()

    is_part_two = args.part == 2
    formatted_day = f"{args.day:02d}"
    module_name = f"day_{formatted_day}"
    base_dir = Path.cwd() / module_name

    if not base_dir.is_dir():
        raise FileNotFoundError(
            f"'{module_name}' does not exist or is not a directory."
        )

    module = import_module(module_name)

    input_file_name = "example_input.txt" if args.example else "input.txt"
    input_file = base_dir / input_file_name

    if not input_file.exists():
        raise FileNotFoundError(f"'{input_file}' does not exist.")

    prompt = "..."
    if args.prompt:
        with open(base_dir / f"prompt_{'1' if not is_part_two else '2'}.txt", "r") as f:
            prompt = f.read()

    with open(input_file, "r") as f:
        puzzle_input = f.read()

    func = module.part_one if not is_part_two else module.part_two
    puzzle_output = func(puzzle_input)
    print(
        f"""\
Advent Of Code 2022!

+++++++++++++++++++++++++
Day {formatted_day}
Part {'One' if not is_part_two else 'Two'}
+-+-+-+-+-+-+-+-+-+-+-+-+

Prompt:
=========================
{prompt}
-------------------------

Output:
=========================
{puzzle_output}
-------------------------
"""
    )
