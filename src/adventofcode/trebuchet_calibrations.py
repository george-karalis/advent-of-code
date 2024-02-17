"""
Deciphers with accuracy the very scientific, brand new and improved calibration document.
Calculates and recovers with immaculate precision the exact calibration value.
"""

import argparse
import logging
from pathlib import Path
from typing import Generator

logger = logging.getLogger(__spec__.name if __spec__ else __name__)


def input_decipher_iterator(input_file_path: Path) -> Generator:
    """
    ### Calculate each lines's first and last digit sum, from the txt file.
    ---
    """

    with open(input_file_path) as FileObj:
        for line in FileObj:
            print(line)
            break


# TODO: find out how rich could work for the cli.
def parse_arguments(argv: list[str]) -> argparse.Namespace:
    """
    Parse arguments via argv
    """


def main(args):
    input_decipher_iterator()
