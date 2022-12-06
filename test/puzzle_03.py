from src import day_03

from .utils import run_real
from .utils import run_test


def test_puzzle_03():
    run_test(
        {
            "inputs/day_03/example.txt": {
                day_03.part_one: 157,
                day_03.part_two: 70,
            },
            "inputs/day_03/input.txt": {
                day_03.part_one: 7848,
                day_03.part_two: 2616,
            },
        }
    )
    run_real(
        {
            "inputs/day_03/input.txt": {
                day_03.part_one: "outputs/day_03/output_1.txt",
                day_03.part_two: "outputs/day_03/output_2.txt",
            }
        }
    )
