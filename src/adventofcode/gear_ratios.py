"""
# Calculates the sum of all the part numbers given an engine schematic.
"""

import argparse
import re
import numpy as np
from pathlib import Path
from typing import Generator

from adventofcode.settings import INPUT_FILE_PATH, NEIGHBOR_INDEXES
from adventofcode.setup_console import log_error, log_success


class GearRatios:

    def __init__(self, args) -> None:
        self.input_file = args.input_file
        self.grid = self.create_grid()
        self.lines_num, self.chars_num = len(self.grid), len(self.grid[0])
        self.sum = 0

    def create_grid(self) -> list[list[str]]:
        with open(self.input_file, "r") as FileObj:
            lines = FileObj.readlines()
        return [list(line.strip()) for line in lines]

    def scan_schematic_grid(self):
        """
        ### Scan through each character of each line and check if they are valid digits.
        """
        for line_idx in range(self.lines_num):
            valid_position = False
            char_idx = 0
            while char_idx < self.chars_num:
                if not self.grid[line_idx][char_idx].isdigit():
                    char_idx += 1
                    continue
                valid_position = self.check_char_neighbors(line_idx, char_idx)
                digit = self.grid[line_idx][char_idx]
                while self.next_char_is_digit_too(line_idx, char_idx):
                    digit += self.grid[line_idx][char_idx + 1]
                    valid_position = valid_position or self.check_char_neighbors(
                        line_idx, char_idx + 1
                    )
                    char_idx += 1
                char_idx += 1
                if valid_position:
                    self.sum += int(digit)

    def next_char_is_digit_too(self, line_idx: int, char_idx: int) -> bool:
        """
        ### Checks next character if it's digit or not.

        Parameters
        ----------
        line_idx
            Current line index the script scans for digits.
        char_idx
            Current character index, known that it is a digit.

        Returns
        -------
            True if it is a digit False if it is not.
        """

        if (
            char_idx + 1 < self.chars_num
            and self.grid[line_idx][char_idx + 1].isdigit()
        ):
            return True
        return False

    def check_char_neighbors(self, line_idx: int, char_idx: int) -> bool:
        """
        ### Checks the neighboring characters for a symbol.

        Parameters
        ----------
        line_idx
            Line number of the character.
        char_idx
            Index of Character in the line.
        """
        for neighbor_line_idx, neighbor_char_idx in NEIGHBOR_INDEXES:
            line_i = neighbor_line_idx + line_idx
            char_i = neighbor_char_idx + char_idx
            if self.exceeds_length(line_i, char_i):
                continue
            neighbor_character = self.grid[line_i][char_i]
            if neighbor_character.isdigit() or neighbor_character == ".":
                continue
            return True
        return False

    def exceeds_length(self, line_i: int, char_i: int) -> bool:
        """
        ### Assert that we won't scan after the edge of the grid.

        Parameters
        ----------
        line_i
            Line to be scanned
        char_i
            Index of that said Line

        Returns
        -------
            True or False.
        """
        if line_i < 0 or line_i >= self.lines_num:
            return True
        if char_i < 0 or char_i >= self.chars_num:
            return True
        return False

    def engine_parts_sum(self) -> None:
        """
        ### Logs sum.
        """
        log_success(f"Total sum of engine part numbers: {self.sum}")


def parse_arguments(argv: list[str] | None = None) -> argparse.Namespace:
    """
    ### Parse arguments from cli.
    """

    parser = argparse.ArgumentParser(
        allow_abbrev=False,
        description=__doc__,
    )
    parser.add_argument(
        "-in",
        "--input-file",
        type=Path,
        default=Path(INPUT_FILE_PATH, "engine_schematic.txt"),
        help="Pass the input file",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> None:
    """
    ### Get the arguments from cli and find the right part numbers sum
    """

    args = parse_arguments(argv)
    gear_ratios = GearRatios(args)
    gear_ratios.scan_schematic_grid()
    gear_ratios.engine_parts_sum()


if __name__ == "__main__":
    main()
