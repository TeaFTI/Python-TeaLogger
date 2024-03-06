"""
Test TeaLogger
~~~~~~~~~~~~~~

This module test functionality for the TeaLogger.
"""

import logging
import logging.config

import pytest

import tealogger
from tealogger import tealogger


class TestDefaultFormatter:
    """Test Default Formatter

    :param configuration: The configuration fixture
    :type configuration: dict (pytest.FixtureRequest)
    """

    def test_default(
        self,
        configuration: dict
    ):
        """Test Default"""
        logger = logging.getLogger('default-format-logger')
        logging.config.dictConfig(configuration)
        logging.basicConfig(level='DEBUG')
        logger.debug('Debug Message')


class TestTeaLogger:
    """Test TeaLogger"""

    @pytest.mark.parametrize(
        'name, expected', [
            ('tea-logger', tealogger.TeaLogger),
        ]
    )
    def test_init(self, name: str, expected: tealogger.TeaLogger):
        """Test init

        Test init (initialize) of the TeaLogger class
        """
        logger = logging.getLogger(name)
        logger.debug('Logging: Debug Message')
        logger.warning('Logging: Warning Message')
        logger.error('Logging: Error Message')

        # tea_logger = tealogger.TeaLogger(name=name)
        # tea_logger.debug('TeaLogger: Debug Message')
        # tea_logger.warning('TeaLogger: Warning Message')
        # assert isinstance(tea_logger, expected)


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
