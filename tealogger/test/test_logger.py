"""Test Logger

This module test functionality for the logger.
"""

import pytest

from tealogger import logger


def test_initialize():
    """Test initialize of the logger class

    Create an instance of Logger and check to make sure the object
    is of Logger type.
    """

    test_logger = logger.Logger('test-logger')
    assert isinstance(test_logger, logger.Logger)


def test_color_success():
    """Test display of log messages and color

    Create an instance of Logger and log messages using different
    level to display different color.
    """

    test_logger = logger.Logger('test-logger')

    test_logger.debug('Debug Message')
    test_logger.info('Info Message')
    test_logger.warning('Warning Message')
    test_logger.error('Error Message')
    test_logger.critical('Critical Message')
