from src import day_06

from .utils import run_real
from .utils import run_test


def test_puzzle_06():
    run_test(
        {
            "inputs/day_06/example.txt": {
                # day_06.part_one: None,
                # day_06.part_two: None,
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
