"""
Identifies the IDs of the possible games and calculates their sum.
"""

import argparse
from dataclasses import dataclass, field
from pathlib import Path
from typing import Generator


from adventofcode.settings import DEFAULT_CUBES_COUNT, INPUT_FILE_PATH
from adventofcode.setup_console import log_error, log_success


@dataclass
class Cube:
    color: str
    count: int


@dataclass
class GameSet:
    cubes: list[Cube] = field(default_factory=list)


@dataclass
class Game:
    game_id: int
    game_sets: list[GameSet] = field(default_factory=list)


class GameCreator:
    """
    ## Base Game Creator
    """

    def __init__(self, args) -> None:
        self.cubes_combinations = args.input_file

    def game_parser(self) -> Generator:
        """
        ### Generates `Game` objects from strings.

        Yields
        ------
            `Game` objects.
        """
        with open(self.cubes_combinations) as FileObj:
            for game in FileObj:
                game = self.split_game_and_sets(game)
                yield game

    def split_game_and_sets(self, game: str) -> Game:
        """
        ### Get Game Sets Out of the Game.

        Parameters
        ----------
        game
            The game as read from the input file.

        Returns
        -------
            The game as a `Game`

        Raises
        ------
        KeyError
            In the case the game doesn't have a numeric ID.
        """
        game_str, game_sets = game.split(":")
        _, game_id = game_str.split()
        if not game_id.isdigit():
            error_message = f"{game_id} is not a valid ID"
            log_error(error_message)
            raise KeyError(error_message)
        game_sets = game_sets.split(";")
        game_obj = self.get_game_record(game_id, game_sets)

        return game_obj

    def get_game_record(self, game_id: str, game_sets: list[str]) -> Game:
        """
        ### Configure the sets of the game.

        Parameters
        ----------
        game_id
            Each game's ID
        game_sets
            Each game's list of GameSet

        Returns
        -------
            Creates the game itself as a `Game`
        """

        game = Game(game_id=int(game_id))
        for game_set in game_sets:
            game_set_cubes = []
            cubes = game_set.split(",")
            for cube in cubes:
                cube_count, cube_color = cube.split()
                game_set_cubes.append(Cube(color=cube_color, count=int(cube_count)))
            game.game_sets.append(GameSet(cubes=game_set_cubes))
        return game


class ValidGameIDAggregator(GameCreator):
    """
    Calculates the ID Sum of all the Valid Games.

    Parameters
    ----------
    GameCreator
        Inherits the Game from the `GameCreator` Class
    """

    def __init__(self, args) -> None:

        super().__init__(args)
        self.valid_game_id_aggregator = 0

    def game_parser(self) -> None:
        """
        ### Goes through the games and determine their validity.
        """
        for game in super().game_parser():
            game_sets = game.game_sets
            game_validity = self.game_set_validator(game_sets)
            if game_validity:
                self.valid_game_id_aggregator += game.game_id

        log_success(f"Total sum of valid Game IDs: {self.valid_game_id_aggregator}")

    def game_set_validator(self, game_sets: list[GameSet]) -> bool:
        """
        ### Validates game Sets.

        Parameters
        ----------
        game_sets
            list of GameSet

        Returns
        -------
            Validity of the Game.
        """
        for game_set in game_sets:
            for cube in game_set.cubes:
                validity = cube.count <= DEFAULT_CUBES_COUNT[cube.color.upper()]
                if not validity:
                    return validity
        return validity


class GamePowerAggregator(GameCreator):
    """
    ## Calculates the Power Sum of all the Games.

    Parameters
    ----------
    GameCreator
        Inherits the Game from the `GameCreator` Class
    """

    def __init__(self, args) -> None:
        super().__init__(args)
        self.game_power_sum = 0

    def game_parser(self) -> None:
        for game in super().game_parser():
            game_sets = game.game_sets
            self.game_power_sum += self.max_cube_count(game_sets)

        log_success(f"Total Power of all Games: {self.game_power_sum}")

    def max_cube_count(self, game_sets: list[GameSet]) -> int:
        """
        What is the least count for each cube color that would be sufficient for the game to be valid?
        This question is answered in this method, alongside the calculation of the power of the Game.

        Parameters
        ----------
        game_sets
            List of `GameSet`

        Returns
        -------
            The Power of the Game.
        """
        min_red_count, min_blue_count, min_green_count = 0, 0, 0
        for game_set in game_sets:
            for cube in game_set.cubes:
                if cube.color == "red":
                    min_red_count = max(cube.count, min_red_count)
                elif cube.color == "blue":
                    min_blue_count = max(cube.count, min_blue_count)
                else:
                    min_green_count = max(cube.count, min_green_count)

        game_set_power = min_green_count * min_red_count * min_blue_count

        return game_set_power


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
    """
    ### Get the arguments from cli and execute the Game Calculations.
    """
    args = parse_arguments(argv)
    valid_game_ids = ValidGameIDAggregator(args)
    valid_game_ids.game_parser()
    game_power = GamePowerAggregator(args)
    game_power.game_parser()


if __name__ == "__main__":
    main()
