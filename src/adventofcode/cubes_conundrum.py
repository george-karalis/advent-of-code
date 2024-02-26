"""
Identifies the IDs of the possible games and calculates their sum.
"""

import argparse
from dataclasses import dataclass
from pathlib import Path

import Exception

from adventofcode.settings import DEFAULT_CUBES_COUNT, INPUT_FILE_PATH


class InvalidNumberOfCubes(Exception):
    """
    ## Raised when a set has at least one number of cubes that exceeds the threshold.
    """

    pass


@dataclass
class Set:
    red_count: int
    green_count: int
    blue_count: int


@dataclass
class Game:
    id: int
    sets = list[Set]


class ValidGameIDAggregator:
    """
    ## Calculate the sum of all the valid Game IDs.
    """

    def __init__(self, args) -> None:

        @dataclass
        class GameSet(Set):

            def __post_init__(self):
                red_invalid = self.red_count > args.red
                blue_invalid = self.blue_count > args.blue
                green_invalid = self.green_count > args.blue

                if any((red_invalid, blue_invalid, green_invalid)):
                    raise InvalidNumberOfCubes

        self.cubes_combinations = args.input_file

        self.set_threshold = GameSet(
            red_count=args.red,
            green_count=args.green,
            blue_count=args.blue,
        )
        self.game_ids_aggregator = 0

    def aggregator(self) -> None:
        """
        ### Calculate the sum of all the valid Game IDs.
        ---
        """
        with open(self.cubes_combinations) as FileObj:
            for game in FileObj:
                pass

    def split_game_to_set(self, game: str) -> Game:
        """ """

    # def validate_game(self, game:):


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
        default=Path(INPUT_FILE_PATH, "cubes_set_input.txt"),
        help="Pass the input file",
    )
    parser.add_argument(
        "-b",
        "--blue",
        type=int,
        default=DEFAULT_CUBES_COUNT.get("BLUE"),
        help="Pass the number of the blue cubes.",
    )
    parser.add_argument(
        "-g",
        "--green",
        type=int,
        default=DEFAULT_CUBES_COUNT.get("GREEN"),
        help="Pass the number of the green cubes.",
    )
    parser.add_argument(
        "-r",
        "--red",
        type=int,
        default=DEFAULT_CUBES_COUNT.get("RED"),
        help="Pass the number of the red cubes.",
    )

    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> None:
    args = parse_arguments(argv)


if __name__ == "__main__":
    main()
