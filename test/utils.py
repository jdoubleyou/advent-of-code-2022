import logging
from pathlib import Path

import pytest


def run_test(details):
    base_dir = Path.cwd()
    for file, cases in details.items():
        with open(base_dir / file, "r") as f:
            logging.debug(f"reading {base_dir / file}")
            contents = f.read()
            logging.debug(f"contents ({base_dir / file}): " + contents)
            if not cases:
                pytest.skip("No test cases to run.")
            for func, expected in cases.items():
                assert expected == func(contents)


def run_real(details):
    base_dir = Path.cwd()
    for in_file, cases in details.items():
        with open(base_dir / in_file, "r") as f:
            logging.debug(f"reading {base_dir / in_file}")
            contents = f.read()
            logging.debug(f"contents ({base_dir / in_file}): " + contents)
            for func, out_file in cases.items():
                with open(base_dir / out_file, "w") as out:
                    logging.debug(f"writing {base_dir / out_file}")
                    result = str(func(contents))
                    result_message = f"RESULT ({func.__name__}): {result}"
                    out.write(result_message)
                    logging.info(result_message)
                    print("\n    " + result_message, end="")
            print()
