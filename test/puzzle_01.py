from src import day_01

from .utils import run_real
from .utils import run_test


def test_puzzle():
    run_test(
        {
            "inputs/day_01/example.txt": {
                day_01.part_one: 24000,
                day_01.part_two: 45000,
            },
            "inputs/day_01/input.txt": {
                day_01.part_one: 70698,
                day_01.part_two: 206643,
            },
        }
    )
    run_real(
        {
            "inputs/day_01/input.txt": {
                day_01.part_one: "outputs/day_01/output_1.txt",
                day_01.part_two: "outputs/day_01/output_2.txt",
            }
        }
    )
