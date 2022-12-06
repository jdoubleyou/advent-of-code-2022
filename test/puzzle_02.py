from src import day_02

from .utils import run_real
from .utils import run_test


def test_puzzle():
    run_test(
        {
            "inputs/day_02/example.txt": {
                day_02.part_one: 15,
                day_02.part_two: 12,
            },
            "inputs/day_02/input.txt": {
                day_02.part_one: 12458,
                day_02.part_two: 12683,
            },
        }
    )
    run_real(
        {
            "inputs/day_02/input.txt": {
                day_02.part_one: "outputs/day_02/output_1.txt",
                day_02.part_two: "outputs/day_02/output_2.txt",
            }
        }
    )
