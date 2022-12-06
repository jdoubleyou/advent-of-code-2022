# from src import day_07

from .utils import run_real
from .utils import run_test


def test_puzzle_07():
    run_test(
        {
            "inputs/day_07/example.txt": {
                # day_07.part_one: None,
                # day_07.part_two: None,
            },
        }
    )
    run_real(
        {
            "inputs/day_07/input.txt": {
                # day_07.part_one: "outputs/day_06/output_1.txt",
                # day_07.part_two: "outputs/day_06/output_2.txt",
            }
        }
    )
