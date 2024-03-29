"""
Contains all the necessary hard coded data, that each puzzle requires in order to reach to its resolution.
"""

from pathlib import Path

import adventofcode

INPUT_FILE_PATH = Path(Path(adventofcode.__file__).parent, "assets")

# Day1: Collections of strings to be identify while scanning the calibration document

NUMERICAL_DIGITS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
ALPHA_DIGITS = [
    "zero",
    "orez",
    "one",
    "eno",
    "two",
    "owt",
    "three",
    "eerht",
    "four",
    "ruof",
    "five",
    "evif",
    "six",
    "xis",
    "seven",
    "neves",
    "eight",
    "thgie",
    "nine",
    "enin",
]

# Day2: Max Available Cubes

DEFAULT_CUBES_COUNT = {
    "RED": 12,
    "GREEN": 13,
    "BLUE": 14,
}


# Day 3: Neighbor Indexes

NEIGHBOR_INDEXES = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
]
