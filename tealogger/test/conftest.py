"""
Configure Test
~~~~~~~~~~~~~~

This module implement test configuration for Tea Logger.
"""

from itertools import product
import json
from pathlib import Path
import platform
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
# conftest_logger = tealogger.get_logger(name=__name__)

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
    conftest_logger.debug(f'Metafunc: {metafunc}')
    conftest_logger.debug(f'Module Name: {metafunc.module.__name__}')
    conftest_logger.debug(f'Class Name: {metafunc.cls.__name__}')
    conftest_logger.debug(f'Function Name: {metafunc.function.__name__}')
    conftest_logger.debug(f'Fixture Names: {metafunc.fixturenames}')

    # Parse metafunc name
    module_name = metafunc.module.__name__.split('.')[-1]
    class_name = metafunc.cls.__name__
    function_name = metafunc.function.__name__

    # Load the test data
    if (Path(__file__).parent / f'{module_name}.json').exists():
        test_data_path = Path(__file__).parent / f'{module_name}.json'
    elif (Path(__file__).parent / 'data.json').exists():
        test_data_path = Path(__file__).parent / 'data.json'

    try:
        with open(test_data_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
    except FileNotFoundError as error:
        conftest_logger.warning(f'No Test Data Found: {module_name}')

    # Module Level
    if (
        module_name in data
        and class_name in data[module_name]
        and function_name in data[module_name][class_name]
    ):
        conftest_logger.debug('Generate Module Test')
        test_data = data[module_name][class_name][function_name]['data']
        conftest_logger.debug(f'Test Data: {test_data}')

        argument_name_list = test_data.keys()
        argument_value_list = test_data.values()

        strategy = data[module_name][class_name][function_name]['strategy']

        match strategy:
            case 'product':
                # Create the cartesian product of the argument value to test
                product_value_list = product(*argument_value_list)
            case _:
                # Create a zip of the argument value to test
                product_value_list = zip(*argument_value_list)

        # argument_name_list = list(argument_name_list)
        # product_value_list = list(product_value_list)

        conftest_logger.debug(f'Argument Name List: {argument_name_list}')
        conftest_logger.debug(f'Argument Value List: {argument_value_list}')
        conftest_logger.debug(f'Product Value List: {product_value_list}')

        # Parametrize the test(s), only if test_data is available
        metafunc.parametrize(
            argnames=argument_name_list,
            argvalues=product_value_list,
        )

    # Class Level
    elif class_name in data:
        conftest_logger.debug('Generate Class Test')

    # Function Level
    elif function_name in data:
        conftest_logger.debug('Generate Function Test')


def pytest_addoption(parser: Parser, pluginmanager: PytestPluginManager):
    """Register Command Line Option(s)

    Register argparse style options and ini style config values, called
    once at the beginning of a test run.

    :param parser: The parser for command line option(s)
    :type parser: pytest.Parser
    :param pluginmanager: The pytest plugin manager
    :type pluginmanager: pytest.PytestPluginManager
    """
    conftest_logger.info('pytest Add Option')
    conftest_logger.debug(f'Parser: {parser}')
    conftest_logger.debug(f'Plugin Manager: {pluginmanager}')


def pytest_configure(config: Config) -> None:
    """Configure Test

    Allow perform of initial configuration.

    :param config: The pytest config object
    :type config: pytest.Config
    """
    conftest_logger.info('pytest Configure')
    conftest_logger.debug(f'Config: {config}')


def pytest_sessionstart(session: Session) -> None:
    """Start Session

    Called after the Session object has been created and before
    performing collection and entering the run test loop.

    :param session: The pytest session object
    :type session: pytest.Session
    """
    conftest_logger.info('pytest Session Start')
    conftest_logger.debug(f'Session: {session}')

    conftest_logger.debug('Platform Information')
    conftest_logger.debug(f'Architecture: {platform.architecture()}')
    conftest_logger.debug(f'Machine: {platform.machine()}')
    conftest_logger.debug(f'Node: {platform.node()}')
    conftest_logger.debug(f'Platform: {platform.platform()}')
    conftest_logger.debug(f'Processor: {platform.processor()}')
    conftest_logger.debug(f'Python Build: {platform.python_build()}')
    conftest_logger.debug(f'Python Compiler: {platform.python_compiler()}')
    conftest_logger.debug(f'Python Branch: {platform.python_branch()}')
    conftest_logger.debug(f'Python Implementation: {platform.python_implementation()}')
    conftest_logger.debug(f'Python Revision: {platform.python_revision()}')
    conftest_logger.debug(f'Python Version: {platform.python_version()}')
    conftest_logger.debug(f'Python Version Tuple: {platform.python_version_tuple()}')
    conftest_logger.debug(f'Release: {platform.release()}')
    conftest_logger.debug(f'System: {platform.system()}')
    conftest_logger.debug(f'Version: {platform.version()}')
    conftest_logger.debug(f'Unix Name: {platform.uname()}')


def pytest_sessionfinish(session: Session, exitstatus: Union[int, ExitCode]):
    """Finish Session

    :param session: The pytest session object
    :type session: pytest.Session
    :param exitstatus: The status which pytest will return to the system
    :type exitstatus: Union[int, pytest.ExitCode]
    """
    conftest_logger.info('pytest Session Finish')
    conftest_logger.debug(f'Session: {session}')
    conftest_logger.debug(f'Exit Status: {exitstatus}')


def pytest_unconfigure(config: Config):
    """Unconfigure Test

    Called before test process is exited

    :param config: The pytest config object
    :type config: pytest.Config
    """
    conftest_logger.info('pytest Unconfigure')
    conftest_logger.debug(f'Config: {config}')


@pytest.fixture(scope='function')
def function_logger():
    """Function Logger"""
    pass


@pytest.fixture(scope='class')
def class_logger():
    """Class Logger"""
    pass
