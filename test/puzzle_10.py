# from src import day_10

from .utils import run_real
from .utils import run_test


def test_puzzle_10():
    run_test(
        {
            "inputs/day_10/example.txt": {
                # day_10.part_one: None,
                # day_10.part_two: None,
            },
        }
    )
    run_real(
        {
            "inputs/day_10/input.txt": {
                # day_10.part_one: "outputs/day_06/output_1.txt",
                # day_10.part_two: "outputs/day_06/output_2.txt",
            }
        }
    )
