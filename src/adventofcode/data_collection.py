"""
Contains all the necessary hard coded data, that each puzzle requires in order to reach to its resolution.
"""

from dataclasses import dataclass

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

# Day2: Satchel contents


@dataclass(frozen=True)
class Satchel:
    red_count: int
    green_count: int
    blue_count: int


SATCHEL = Satchel(
    red_count=12,
    green_count=13,
    blue_count=14,
)
