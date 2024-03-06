"""
Test Configuration
~~~~~~~~~~~~~~~~~~

The `conftest` module implement test configuration to test TeaLogger.
"""

import json
from os import PathLike
from pathlib import Path

import pytest


CURRENT_MODULE_PATH: PathLike = Path(__file__).parent.expanduser().resolve()


def load_json_file(path: PathLike) -> dict:
    """Load a JSON (JavaScript Object Notation) file.

    :param path: The path to the JSON file
    :type path: PathLike
    :returns: The JSON data as a dictionary
    :rtype: dict
    """

    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    return data


@pytest.fixture(scope='session')
def configuration():
    """Configuration"""
    configuration_path = CURRENT_MODULE_PATH.parent / 'configuration/default.json'

    return load_json_file(configuration_path)
