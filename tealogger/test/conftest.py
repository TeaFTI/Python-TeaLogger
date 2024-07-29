"""
Configure Test
~~~~~~~~~~~~~~

This module implement test configuration for Tea Logger.
"""

from itertools import product
import json
from pathlib import Path
from typing import Union

import pytest
from pytest import (
    Config,
    ExitCode,
    Metafunc,
    Parser,
    PytestPluginManager,
    Session
)

import tealogger

# Configure conftest_logger
conftest_logger = tealogger.TeaLogger(name=__name__)
conftest_logger.setLevel(tealogger.DEBUG)

def pytest_generate_tests(metafunc: Metafunc):
    """Generate Test Hook

    Dynamically parametrize test(s) using test data from a JSON
    (JavaScript Object Notation) file. The data will align with the
    class and function name of the test(s).

    Example:
        {
            "module_name":
                "ClassName": {
                    "function_name": {
                        "parameter": [
                            "expression",
                            ...
                        ],
                        ...
                    },
                    ...
                },
                ...
            },
            ...
        }

    :param metafunc: Objects passed to the pytest_generate_tests hook
    :type metafunc: pytest.Metafunc
    """
    conftest_logger.info('pytest Generate Test')
    tealogger.debug('Metafunc: %s', metafunc)
    tealogger.debug(f'Module Name: {metafunc.module.__name__}')
    tealogger.debug(f'Class Name: {metafunc.cls.__name__}')
    tealogger.debug(f'Function Name: {metafunc.function.__name__}')
    tealogger.debug(f'Fixture Names: {metafunc.fixturenames}')

    # Load the test data
    with open(Path(__file__).parent / 'data.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Parse metafunc name
    module_name = metafunc.module.__name__.split('.')[-1]
    class_name = metafunc.cls.__name__
    function_name = metafunc.function.__name__

    # Module Level
    if (
        module_name in data
        and class_name in data[module_name]
        and function_name in data[module_name][class_name]
    ):
        tealogger.debug('Generate Module Test')
        test_data = data[module_name][class_name][function_name]['data']
        tealogger.debug('Test Data: %s', test_data)

        argument_name_list = test_data.keys()
        argument_value_list = test_data.values()

        is_product = data[module_name][class_name][function_name]['product']
        if is_product:
            # Create the cartesian product of the argument value to test
            product_value_list = product(*argument_value_list)
        else:
            # Create a zip of the argument value to test
            product_value_list = zip(*argument_value_list)

        # argument_name_list = list(argument_name_list)
        # product_value_list = list(product_value_list)

        tealogger.debug('Argument Name List: %s', argument_name_list)
        tealogger.debug('Argument Value List: %s', argument_value_list)
        tealogger.debug('Product Value List: %s', product_value_list)

        # Parametrize the test(s), only if test_data is available
        metafunc.parametrize(
            argnames=argument_name_list,
            argvalues=product_value_list,
        )

    # Class Level
    elif class_name in data:
        tealogger.debug('Generate Class Test')

    # Function Level
    elif function_name in data:
        tealogger.debug('Generate Function Test')


def pytest_addoption(parser: Parser, pluginmanager: PytestPluginManager):
    """Register Command Line Option(s)

    Register argparse style options and ini style config values, called
    once at the beginning of a test run.

    :param parser: The parser for command line option(s)
    :type parser: pytest.Parser
    :param pluginmanager: The pytest plugin manager
    :type pluginmanager: pytest.PytestPluginManager
    """
    tealogger.info('pytest Add Option')
    tealogger.debug('Parser: %s', parser)
    tealogger.debug('Plugin Manager: %s', pluginmanager)


def pytest_configure(config: Config) -> None:
    """Configure Test

    Allow perform of initial configuration.

    :param config: The pytest config object
    :type config: pytest.Config
    """
    tealogger.info('pytest Configure')
    tealogger.debug('Config: %s', config)


def pytest_sessionstart(session: Session) -> None:
    """Start Session

    Called after the Session object has been created and before
    performing collection and entering the run test loop.

    :param session: The pytest session object
    :type session: pytest.Session
    """
    tealogger.info('pytest Session Start')
    tealogger.debug('Session: %s', session)


def pytest_sessionfinish(session: Session, exitstatus: Union[int, ExitCode]):
    """Finish Session

    :param session: The pytest session object
    :type session: pytest.Session
    :param exitstatus: The status which pytest will return to the system
    :type exitstatus: Union[int, pytest.ExitCode]
    """
    tealogger.info('pytest Session Finish')
    tealogger.debug(f'Session: {session}')
    tealogger.debug(f'Exit Status: {exitstatus}')


def pytest_unconfigure(config: Config):
    """Unconfigure Test

    Called before test process is exited

    :param config: The pytest config object
    :type config: pytest.Config
    """
    tealogger.info('pytest Unconfigure')
    tealogger.debug(f'Config: {config}')


@pytest.fixture(scope='function')
def function_logger():
    """Function Logger"""
    pass


@pytest.fixture(scope='class')
def class_logger():
    """Class Logger"""
    pass
