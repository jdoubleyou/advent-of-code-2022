# from src import day_09

from .utils import run_real
from .utils import run_test


def test_puzzle_09():
    run_test(
        {
            "inputs/day_09/example.txt": {
                # day_09.part_one: None,
                # day_09.part_two: None,
            },
        }
    )
    run_real(
        {
            "inputs/day_09/input.txt": {
                # day_09.part_one: "outputs/day_06/output_1.txt",
                # day_09.part_two: "outputs/day_06/output_2.txt",
            }
        }
    )
