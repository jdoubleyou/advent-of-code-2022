import argparse
import sys
from dataclasses import dataclass
from importlib import import_module
from io import TextIOWrapper
from pathlib import Path
from textwrap import indent
from typing import Any
from typing import Callable

import colorama

from utils import *

list = BetterList
str = BetterStr


class InvalidExpectationError(Exception):
    pass


class UnreadContents:
    pass


class ExpectationUnset:
    pass


@dataclass(init=False)
class TestCase:
    module: str
    func: str
    input_file: str
    expected: str

    def __init__(
        self,
        module: str,
        func: str,
        input_file: str,
        expected: str,
    ) -> None:
        self.module = import_module(module)
        self.func = getattr(self.module, func)
        self.input_file: TextIOWrapper = open(
            (Path.cwd() / module / input_file).absolute(), "r"
        )
        self.expected = expected if expected != "-" else None
        self.contents = UnreadContents()

    @classmethod
    def to(cls, args):
        try:
            return cls(*args)
        except ModuleNotFoundError:
            return None

    def result(self) -> tuple[Any, bool]:
        self.contents = self.input_file.read()
        res = self.func(self.contents, BetterList(self.contents.splitlines()))
        if self.expected is None:
            return res, False
        return res, self.expected == res

    def close(self):
        if not self.input_file.closed:
            self.input_file.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("day", type=int, choices=tuple(range(1, 26)))
    parser.add_argument("part", type=int, choices=(1, 2))
    parser.add_argument("--prompt", action="store_true")
    parser.add_argument("--test", action="store_true")
    args = parser.parse_args()

    split: Callable[
        [str], Callable[[str], BetterList]
    ] = lambda delimiter: lambda s: BetterList(s.split(delimiter))
    strip = lambda s: s.strip()
    non_comments = lambda line: not line.startswith("#")

    part = args.part - 1
    formatted_part = "One" if not args.part else "Two"
    formatted_day = f"{args.day:02d}"
    module_name = f"day_{formatted_day}"
    base_dir = Path.cwd() / module_name
    prompt_file_name = base_dir / f"prompt_{args.part}.txt"
    funcs = ["part_one", "part_two"]
    part_func_name = funcs[part]

    try:
        if not base_dir.is_dir():
            raise FileNotFoundError(
                f"'{module_name}' does not exist or is not a directory."
            )

        module = import_module(module_name)
        func = getattr(module, funcs[part])

        if args.test:
            to_failure_message = (
                lambda triple: f"""\
Expected: {colorama.Fore.GREEN}{triple[0].expected}{colorama.Fore.RESET}
Given:    {colorama.Fore.RED}{triple[1]}{colorama.Fore.RESET}
Input:
{'-' * 32}
{indent(triple[0].contents, "|> ", predicate=lambda s: True)}
{'-' * 32}
    """
            )
            current_day = (
                lambda test_case: test_case and test_case.module.__name__ == module_name
            )
            print_err = lambda s: print(s, file=sys.stderr)
            buffer = "+" * 64
            color_failure = (
                lambda s: colorama.Back.LIGHTRED_EX + s + colorama.Back.RESET
            )
            color_success = (
                lambda s: colorama.Fore.LIGHTGREEN_EX + s + colorama.Fore.RESET
            )
            failures = list()
            with open("tests", "r") as tests_file:
                total_count = IntWrapper(0)
                failure_count = IntWrapper(0)
                to_case_fail_text = (
                    lambda enumerated: f"*** {colorama.Fore.MAGENTA}{enumerated[0]+1}/{failure_count.get()} failed test cases{colorama.Fore.RESET} ***\n{enumerated[1]}"
                )
                successes, failures = (
                    failures.concat(tests_file.readlines())
                    .filter_to(non_comments)
                    .split_each_on("|")
                    .map(lambda strings: strings.map(strip))
                    .map(TestCase.to)
                    .filter_to(current_day)
                    .foreach(total_count.increment)
                    .map(lambda test_case: (test_case,) + test_case.result())
                    .divide(lambda triple: bool(triple[2]))
                )
                # successes.map(to_success_message)
                failures = (
                    failures.foreach(failure_count.increment)
                    .map(to_failure_message)
                    .enumerate()
                    .map(to_case_fail_text)
                )

            if len(failures):
                failures = failures.join("\n").indent(" " * 4)
                totals_row = (
                    f"\n"
                    + color_failure(
                        f"{failure_count} test case{'s' if (failure_count-1) else ''} failed out of {total_count} total test cases run."
                    )
                    + "\n"
                )
                print(
                    buffer + totals_row + "\n" + failures + totals_row + buffer,
                    file=sys.stderr,
                )
                exit(-1)
            print(color_success("*** All Tests successful ***"))
        else:
            input_file = base_dir / "input.txt"

            if not input_file.exists():
                raise FileNotFoundError(f"'{input_file}' does not exist.")

            prompt = "..."
            if args.prompt:
                with open(prompt_file_name, "r") as f:
                    prompt = f.read()

            with open(input_file, "r") as f:
                puzzle_input: str = f.read()

            puzzle_output = func(puzzle_input, BetterList(puzzle_input.splitlines()))
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
    except Exception as e:
        # print("ERROR:\n++++++\n" + str(e) + "\n++++++")
        raise e
