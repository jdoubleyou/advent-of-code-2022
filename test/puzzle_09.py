from src import day_09

from .utils import verify


def test_puzzle_09():
    verify(
        day_09,
        test={
            "example.txt": (None, None),
        },
        real=["input.txt"],
    )
