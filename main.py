import argparse
import sys
from importlib import import_module
from pathlib import Path
from textwrap import indent

import colorama

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("day", type=int, choices=tuple(range(1, 26)))
    parser.add_argument("part", type=int, choices=(1, 2))
    parser.add_argument("--prompt", action="store_true")
    parser.add_argument("--test", action="store_true")
    args = parser.parse_args()

    part = args.part - 1
    formatted_part = "One" if not args.part else "Two"
    formatted_day = f"{args.day:02d}"
    module_name = f"day_{formatted_day}"
    base_dir = Path.cwd() / module_name
    prompt_file_name = base_dir / f"prompt_{args.part}.txt"
    funcs = ["part_one", "part_two"]
    part_func_name = funcs[part]

    if not base_dir.is_dir():
        raise FileNotFoundError(
            f"'{module_name}' does not exist or is not a directory."
        )

    module = import_module(module_name)
    func = getattr(module, funcs[part])

    if args.test:
        test_module_name = "test"
        if not (base_dir / f"{test_module_name}.py").exists():
            raise FileNotFoundError(
                f"'{module_name}' does not have a '{test_module_name}.py' file"
            )
        test_module = import_module(f"{module_name}.{test_module_name}")
        failures = []
        test_cases = getattr(test_module, "test_cases")
        for answers, input_text in test_cases.items():
            result = func(input_text)
            failure_message = f"""\
Expected: {colorama.Fore.GREEN}{answers[part]}{colorama.Fore.RESET}
Given:    {colorama.Fore.RED}{result}{colorama.Fore.RESET}
Input:
{'-' * 32}
{indent(input_text, "|> ")}{'-' * 32}
"""
            if answers[part] != result:
                failures.append(failure_message)
        if len(failures):
            failures = [
                f"*** {colorama.Fore.MAGENTA}{index+1}/{len(failures)} failed test cases{colorama.Fore.RESET} ***\n{msg}"
                for index, msg in enumerate(failures)
            ]
            totals_row = f"\n{colorama.Back.LIGHTRED_EX}{len(failures)} test case{'s' if (len(failures)-1) else ''} failed out of {len(test_cases)} total.{colorama.Back.RESET}\n"
            print(
                ("+" * 64)
                + totals_row
                + "\n"
                + indent("\n".join(failures), " " * 4)
                + totals_row
                + ("+" * 64),
                file=sys.stderr,
            )
            exit(-1)
        print(
            colorama.Fore.LIGHTGREEN_EX
            + "*** All Tests successful ***"
            + colorama.Fore.RESET
        )
    else:
        input_file = base_dir / "input.txt"

        if not input_file.exists():
            raise FileNotFoundError(f"'{input_file}' does not exist.")

        prompt = "..."
        if args.prompt:
            with open(prompt_file_name, "r") as f:
                prompt = f.read()

        with open(input_file, "r") as f:
            puzzle_input = f.read()

        puzzle_output = func(puzzle_input)
        print(
            f"""\
Advent Of Code 2022!

+++++++++++++++++++++++++
Day {formatted_day}
Part {formatted_part}
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
