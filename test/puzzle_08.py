from src import day_08

from .utils import run_real
from .utils import run_test


def test_puzzle_08():
    run_test(
        {
            "inputs/day_08/example.txt": {
                day_08.part_one: None,
                day_08.part_two: None,
            },
            # "inputs/day_08/example2.txt": {
            #     # day_08.part_one: None,
            #     # day_08.part_two: None,
            # },
            # "inputs/day_08/example3.txt": {
            #     # day_08.part_one: None,
            #     # day_08.part_two: None,
            # },
            # "inputs/day_08/example4.txt": {
            #     # day_08.part_one: None,
            #     # day_08.part_two: None,
            # },
        }
    )
    run_real(
        {
            "inputs/day_08/input.txt": {
                day_08.part_one: "outputs/day_08/output_1.txt",
                day_08.part_two: "outputs/day_08/output_2.txt",
            }
        }
    )
