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
        # self.digits_positions = []
        # self.adjacent_positions = {}

    def create_grid(self) -> list[list[str]]:
        with open(self.input_file, "r") as FileObj:
            lines = FileObj.readlines()
        return [list(line.strip()) for line in lines]

    def scan_schematic_grid(self):
        """
        ### Scan through each character of each line and check if they are valid digits.
        """
        for line_idx in range(self.lines_num):
            for char_idx in range(self.chars_num):
                # char = self.grid[line_idx][char_idx]
                if not self.grid[line_idx][char_idx].isdigit():
                    continue
                valid_number = self.check_char_neighbors(line_idx, char_idx)



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










    def get_valid_positions(self) -> dict[int, list[tuple[int]]]:
        """
         ### Create Records of Valid Positions in each line.

        Parameters
        ----------
        lines
            _description_

        Returns
        -------
            _description_
        """
        for line_number, line in self.parse_lines():
            if line_number == 0:
                self.adjacent_positions[line_number] = []
            elif line_number == len(self.lines):

            self.adjacent_positions[line_number + 1] = []
            for char_idx, char in enumerate(line):
                if char.isdigit() or char == ".":
                    continue
                self.adjacent_positions[line_number].append(
                    self.create_adjacent_positions(char_idx)
                )

    def create_adjacent_positions(self, char_idx: int) -> tuple[int]:
        """
        ### Identifies all the neighboring positions to the character.

        Parameters
        ----------
        line_number
            Line of special Character
        char_idx
            Index in Line the Character was found

        Returns
        -------
            The Neighboring positions of the Character.
        """


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


if __name__ == "__main__":
    main()
