"""
Deciphers with accuracy the very scientific, brand new and improved calibration document.
Calculates and recovers with immaculate precision the exact calibration value.
"""

import argparse
import logging
import sys
from pathlib import Path

logger = logging.getLogger(__spec__.name if __spec__ else __name__)


def calibrate(input_file_path: Path) -> None:
    """
    ### Calculate each lines's first and last digit sum, from the txt file.
    ---
    """
    calibration_value = 0
    with open(input_file_path) as FileObj:
        for line in FileObj:
            calibration_value += get_first_and_last_digit(line)

    logger.info(f"Calibration value: {calibration_value}")


def get_first_and_last_digit(line: str) -> int:
    """
    ### Returns the first and last digits for a line as a 2-digit int.
    ---
    """
    digits_in_line = [digit for digit in line if digit.isdigit()]
    if not len(digits_in_line):
        raise KeyError(f"No digit found in line: {line}")

    return int(digits_in_line[0] + digits_in_line[-1])


# TODO: find out how rich could work for the cli.
def parse_arguments(argv: list[str] | None = None) -> argparse.Namespace:
    """
    ### Parse arguments via argv.
    ---
    """
    parser = argparse.ArgumentParser(
        allow_abbrev=False,
        description=__doc__,
    )
    parser.add_argument(
        "-in", "--input-file", type=Path, help="Add the input file path."
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> None:
    args = parse_arguments(argv)

    streamHandler = logging.StreamHandler(sys.stdout)
    logger.addHandler(streamHandler)
    logger.setLevel(logging.INFO)

    calibrate(args.input_file)


if __name__ == "__main__":
    main()
