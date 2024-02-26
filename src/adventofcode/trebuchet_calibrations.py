"""
Deciphers with accuracy the very scientific, brand new and improved calibration document.
Calculates and recovers with immaculate precision the exact calibration value.
"""

import argparse
import re
from pathlib import Path

from word2number import w2n

from adventofcode.settings import ALPHA_DIGITS, INPUT_FILE_PATH, NUMERICAL_DIGITS
from adventofcode.setup_console import log_error, log_success

digit_scanner_method = {1: NUMERICAL_DIGITS, 2: NUMERICAL_DIGITS + ALPHA_DIGITS}


class Calibrate:
    """
    ## Calibrate Trebuchet accurately.
    """

    def __init__(self, args) -> None:
        self.calibration_doc = args.input_file
        self.scan_pattern = digit_scanner_method.get(args.scan_method, NUMERICAL_DIGITS)
        self.calibration_value = 0

    def calibrate(self) -> None:
        """
        ### Calculate each lines's first and last digit sum, from the txt file.
        ---
        """

        with open(self.calibration_doc) as FileObj:
            for line in FileObj:
                self.calibration_value += self.get_first_and_last_digit(line)

        log_success(f"Calibration value: {self.calibration_value}")

    def get_first_and_last_digit(self, line: str) -> int:
        """
        ### Returns the first and last digits for a line as a 2-digit int.
        ---
        """

        pattern = "|".join(self.scan_pattern)
        first_digit = re.findall(pattern, line)
        last_digit = re.findall(pattern, line[::-1])

        if not len(first_digit):
            log_error(f"No digit found in line: {line}")
            raise KeyError(f"No digit found in line: {line}")

        string_digits = [first_digit[0], last_digit[0][::-1]]
        digits_in_line = [str(w2n.word_to_num(digit)) for digit in string_digits]

        return int(digits_in_line[0] + digits_in_line[-1])


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
        "-in",
        "--input-file",
        type=Path,
        default=Path(INPUT_FILE_PATH, "calibration_doc_input.txt"),
        help="Add the input file path.",
    )
    parser.add_argument(
        "--scan_method",
        type=int,
        default=1,
        choices=[1, 2],
        help="Different Day Same Problem, Different Approach. Select the Day to Select the Approach",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> None:
    args = parse_arguments(argv)

    calibrate = Calibrate(args)
    calibrate.calibrate()


if __name__ == "__main__":
    main()
