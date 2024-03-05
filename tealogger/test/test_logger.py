"""Test Logger

This module test functionality for the logger.
"""

from tealogger import tealogger


def test_initialize():
    """Test initialize of the logger class

    Create an instance of Logger and check to make sure the object
    is of Logger type.
    """

    test_logger = tealogger.TeaLogger('test-logger')
    assert isinstance(test_logger, tealogger.TeaLogger)


def test_short_record_format():
    """Test short format log

    Create an instance of Logger, and set the formatter using
    `SHORT_RECORD_FORMAT`, and log messages using different level
    """
    test_logger = tealogger.TeaLogger('test-logger')

    test_logger.set_formatter(
        record_format=tealogger.SHORT_RECORD_FORMAT,
        )

    test_logger.debug('Debug Message')
    test_logger.info('Info Message')
    test_logger.warning('Warning Message')
    test_logger.error('Error Message')
    test_logger.critical('Critical Message')


def test_color_success():
    """Test display of log messages and color

    Create an instance of Logger and log messages using different
    level to display different color.
    """

    test_logger = tealogger.TeaLogger('test-logger')

    test_logger.debug('Debug Message')
    test_logger.info('Info Message')
    test_logger.warning('Warning Message')
    test_logger.error('Error Message')
    test_logger.critical('Critical Message')
