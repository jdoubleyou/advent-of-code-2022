from src import day_05

from .utils import run_real
from .utils import run_test


def test_puzzle_05():
    run_test(
        {
            "inputs/day_05/example.txt": {
                day_05.part_one: "CMZ",
                day_05.part_two: "MCD",
            },
            "inputs/day_05/input.txt": {
                day_05.part_one: "VWLCWGSDQ",
                day_05.part_two: "TCGLQSLPW",
            },
        }
    )
    run_real(
        {
            "inputs/day_05/input.txt": {
                day_05.part_one: "outputs/day_05/output_1.txt",
                day_05.part_two: "outputs/day_05/output_2.txt",
            }
        }
    )
