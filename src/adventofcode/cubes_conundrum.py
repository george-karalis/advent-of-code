"""
Identifies the IDs of the possible games and calculates their sum.
"""

import argparse
from pathlib import Path

from adventofcode.settings import DEFAULT_CUBES_COUNT, INPUT_FILE_PATH
from adventofcode.setup_console import log_error, log_success


class GameIDAggregator:
    """
    ## Calculate the sum of all the valid Game IDs.
    """

    def __init__(self, args) -> None:
        self.cubes_combinations = args.input_file

    def aggregator(self) -> None:
        """
        ### Calculate the sum of all the valid Game IDs.
        ---
        """
        valid_game_ids_sum = 0
        with open(self.cubes_combinations) as FileObj:
            for game in FileObj:
                game_id = self.game_referee(game)
                if game_id is None:
                    continue
                valid_game_ids_sum += game_id
        log_success(f"Total sum of valid Game ids: {valid_game_ids_sum}")

    def game_referee(self, game: str) -> int | None:
        """
        Creates Sets from Game line, and validates the number of cubes in each set of the game.
        If all the game sets have valid number of cubes, it returns the game id.
        """
        game_str, game_sets = game.split(":")
        _, game_id = game_str.split()
        if not game_id.isdigit():
            error_message = f"{game_id} is not a valid ID"
            log_error(error_message)
            raise KeyError(error_message)
        game_id = int(game_id)
        game_sets = game_sets.split(";")
        for game_set in game_sets:
            cubes = game_set.split(",")
            for cube in cubes:
                cube_count_valid = self.check_validity(cube)
                if not cube_count_valid:
                    return None
        return game_id

    def check_validity(self, cube: str) -> bool:
        """
        Validates Cube's Count.
        """
        cube_count, cube_color = cube.split()
        cube_max_threshold_count = DEFAULT_CUBES_COUNT.get(cube_color.upper())
        if cube_max_threshold_count is None:
            log_error(f"There shouldn't be any {cube_color} cubes in the bad.")
            return False
        return int(cube_count) <= cube_max_threshold_count


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
    valid_game_ids = GameIDAggregator(args)
    valid_game_ids.aggregator()


if __name__ == "__main__":
    main()
