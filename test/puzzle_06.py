from src import day_06

from .utils import run_real
from .utils import run_test


def test_puzzle_06():
    run_test(
        {
            "inputs/day_06/example.txt": {
                day_06.part_one: 7,
                day_06.part_two: 19,
            },
            "inputs/day_06/example2.txt": {
                day_06.part_one: 5,
                day_06.part_two: 23,
            },
            "inputs/day_06/example3.txt": {
                day_06.part_one: 6,
                day_06.part_two: 23,
            },
            "inputs/day_06/example4.txt": {
                day_06.part_one: 10,
                day_06.part_two: 29,
            },
            "inputs/day_06/example5.txt": {
                day_06.part_one: 11,
                day_06.part_two: 26,
            },
        }
    )
    run_real(
        {
            "inputs/day_06/input.txt": {
                day_06.part_one: "outputs/day_06/output_1.txt",
                day_06.part_two: "outputs/day_06/output_2.txt",
            }
        }
    )
