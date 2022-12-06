from src import day_04

from .utils import run_real
from .utils import run_test


def test_puzzle_04():
    run_test(
        {
            "inputs/day_04/example.txt": {
                day_04.part_one: 2,
                day_04.part_two: 4,
            },
            "inputs/day_04/input.txt": {
                day_04.part_one: 567,
                day_04.part_two: 907,
            },
        }
    )
    run_real(
        {
            "inputs/day_04/input.txt": {
                day_04.part_one: "outputs/day_04/output_1.txt",
                day_04.part_two: "outputs/day_04/output_2.txt",
            }
        }
    )
