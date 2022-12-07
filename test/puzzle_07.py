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
            # "inputs/day_07/example2.txt": {
            #     # day_07.part_one: None,
            #     # day_07.part_two: None,
            # },
            # "inputs/day_07/example3.txt": {
            #     # day_07.part_one: None,
            #     # day_07.part_two: None,
            # },
            # "inputs/day_07/example4.txt": {
            #     # day_07.part_one: None,
            #     # day_07.part_two: None,
            # },
        }
    )
    run_real(
        {
            "inputs/day_07/input.txt": {
                # day_07.part_one: "outputs/day_07/output_1.txt",
                # day_07.part_two: "outputs/day_07/output_2.txt",
            }
        }
    )
