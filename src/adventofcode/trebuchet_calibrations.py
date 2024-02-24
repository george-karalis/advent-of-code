"""
Deciphers with accuracy the very scientific, brand new and improved calibration document.
Calculates and recovers with immaculate precision the exact calibration value.
"""

import argparse
import logging
import re
import sys
from pathlib import Path

from word2number import w2n

from adventofcode.digits_collection import ALPHA_DIGITS, NUMERICAL_DIGITS

logger = logging.getLogger(__spec__.name if __spec__ else __name__)


digit_scanner_method = {1: NUMERICAL_DIGITS + ALPHA_DIGITS}


def calibrate(args: argparse.Namespace) -> None:
    """
    ### Calculate each lines's first and last digit sum, from the txt file.
    ---
    """
    calibration_value = 0
    scanner_lookup = digit_scanner_method.get(args.day)
    if not scanner_lookup:
        raise KeyError(f"{args.day} has not been yet implemented")

    with open(args.input_file) as FileObj:
        for line in FileObj:
            calibration_value += get_first_and_last_digit(line, scanner_lookup)

    logger.info(f"Calibration value: {calibration_value}")


def get_first_and_last_digit(line: str, scanner_lookup: list[str]) -> int:
    """
    ### Returns the first and last digits for a line as a 2-digit int.
    ---
    """

    pattern = "|".join(scanner_lookup)
    first_digit = re.findall(pattern, line)
    last_digit = re.findall(pattern, line[::-1])

    if not len(first_digit):
        raise KeyError(f"No digit found in line: {line}")

    string_digits = [first_digit[0], last_digit[0][::-1]]
    digits_in_line = [str(w2n.word_to_num(digit)) for digit in string_digits]

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
    parser.add_argument(
        "--day",
        type=int,
        default=1,
        help="Different Day Same Problem, Different Approach. Select the Day to Select the Approach",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> None:
    args = parse_arguments(argv)

    streamHandler = logging.StreamHandler(sys.stdout)
    logger.addHandler(streamHandler)
    logger.setLevel(logging.INFO)

    calibrate(args)


if __name__ == "__main__":
    main()
