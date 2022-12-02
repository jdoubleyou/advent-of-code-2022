import argparse
from pathlib import Path


def part_one(puzzle_input):
    return max(
        [
            sum([int(e) for e in elf.split()])
            for elf in puzzle_input.strip().split("\n\n")
        ]
    )


def part_two(puzzle_input):
    return sum(
        list(
            reversed(
                sorted(
                    [
                        sum([int(e) for e in elf.split()])
                        for elf in puzzle_input.strip().split("\n\n")
                    ]
                )
            )
        )[:3]
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--file", default=Path.cwd() / "day-01" / "example_puzzle_input.txt"
    )
    parser.add_argument("--part_two", action="store_true")
    args = parser.parse_args()

    with open(args.file, "r") as f:
        puzzle_input = f.read()

    func = part_one if not args.part_two else part_two
    puzzle_output = func(puzzle_input)
    print(
        f"Puzzle Output For Day 1 (part {'one' if not args.part_two else 'two'}):\n\n{puzzle_output}"
    )
