"""Logger Module

This module implements the Tea Logger.
"""

import logging
import logging.config
from logging import LogRecord
import sys
from typing import (override, Union)


# Log Level
CRITICAL = logging.CRITICAL
FATAL = logging.FATAL
ERROR = logging.ERROR
WARNING = logging.WARNING
WARN = logging.WARN
INFO = logging.INFO
DEBUG = logging.DEBUG
NOTSET = logging.NOTSET

DEFAULT_RECORD_FORMAT = '[%(levelname)s %(name)s %(asctime)s] %(message)s'
DEFAULT_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
SHORT_RECORD_FORMAT = '[%(levelname)-.1s %(asctime)s] %(message)s'

_COLOR_CODE = {
    # Reset
    'RESET': '\x1b[0m',
    # Foreground
    'FOREGROUND_BLACK': '\x1b[30m',
    'FOREGROUND_RED': '\x1b[31m',
    'FOREGROUND_GREEN': '\x1b[32m',
    'FOREGROUND_YELLOW': '\x1b[33m',
    'FOREGROUND_BLUE': '\x1b[34m',
    'FOREGROUND_MAGENTA': '\x1b[35m',
    'FOREGROUND_CYAN': '\x1b[36m',
    'FOREGROUND_WHITE': '\x1b[37m',
    'FOREGROUND_DEFAULT': '\x1b[39m',
    # Background
    'BACKGROUND_BLACK': '\x1b[40m',
    'BACKGROUND_RED': '\x1b[41m',
    'BACKGROUND_GREEN': '\x1b[42m',
    'BACKGROUND_YELLOW': '\x1b[43m',
    'BACKGROUND_BLUE': '\x1b[44m',
    'BACKGROUND_MAGENTA': '\x1b[45m',
    'BACKGROUND_CYAN': '\x1b[46m',
    'BACKGROUND_WHITE': '\x1b[47m',
    'BACKGROUND_DEFAULT': '\x1b[49m',
    # Style
    'STYLE_BOLD': '\x1b[1m',
    'STYLE_DIM': '\x1b[2m',
    'STYLE_UNDERLINED': '\x1b[4m',
    'STYLE_BLINK': '\x1b[5m',
    'STYLE_REVERSE': '\x1b[7m',
    'STYLE_HIDDEN': '\x1b[8m',
    'STYLE_DEFAULT': '\x1b[22m',
}

_LEVEL_COLOR_CODE = {
    'NOTSET': _COLOR_CODE['RESET'],
    'DEBUG': _COLOR_CODE['FOREGROUND_CYAN'],
    'INFO': _COLOR_CODE['FOREGROUND_GREEN'],
    'WARNING': _COLOR_CODE['FOREGROUND_YELLOW'],
    'SUCCESS': _COLOR_CODE['FOREGROUND_GREEN'],
    'ERROR': _COLOR_CODE['FOREGROUND_RED'],
    'CRITICAL': f"{_COLOR_CODE['FOREGROUND_RED']}{_COLOR_CODE['BACKGROUND_WHITE']}",
}


class DefaultFormatter(logging.Formatter):
    """Default Formatter

    Define a default Formatter.
    """

    def __init__(
        self,
        record_format: Union[str, None] = None,
        date_format: Union[str, None] = None
    ) -> None:
        """Constructor

        :param record_format: The record format for the Formatter,
            defaults to `None`, set from configuration
        :type record_format: str, optional
        :param date_format: The date format for the Formatter, defaults
            to `None`, set from configuration
        :type date_format: str, optional
        """
        # Call super class
        super().__init__(fmt=record_format, datefmt=date_format)

        self._level_format = {
            DEBUG: (
                f"{_LEVEL_COLOR_CODE['DEBUG']}"
                f"{record_format}"
                f"{_LEVEL_COLOR_CODE['NOTSET']}"
            ),
            INFO: (
                f"{_LEVEL_COLOR_CODE['INFO']}"
                f"{record_format}"
                f"{_LEVEL_COLOR_CODE['NOTSET']}"
            ),
            WARNING: (
                f"{_LEVEL_COLOR_CODE['WARNING']}"
                f"{record_format}"
                f"{_LEVEL_COLOR_CODE['NOTSET']}"
            ),
            ERROR: (
                f"{_LEVEL_COLOR_CODE['ERROR']}"
                f"{record_format}"
                f"{_LEVEL_COLOR_CODE['NOTSET']}"
            ),
            CRITICAL: (
                f"{_LEVEL_COLOR_CODE['CRITICAL']}"
                f"{record_format}"
                f"{_LEVEL_COLOR_CODE['NOTSET']}"
            ),
        }

        self.date_format = date_format

    @override
    def format(self, record: LogRecord) -> str:
        """Format the specified record as text (redefined)

        :param record: The record to format, used for string formatting
            operation
        :type record: dict

        :return: (str) the formatted record
        """
        log_format = self._level_format.get(record.levelno)
        formatter = logging.Formatter(fmt=log_format, datefmt=self.date_format)

        return formatter.format(record)


class TeaLogger(logging.Logger):
    """TeaLogger class

    A TeaLogger with predefined log format.
    """

    def __init__(
        self,
        name: str,
        level: Union[int, str] = NOTSET,
    ) -> None:
        """Constructor

        :param name: the name of the logger
        :type name: str
        :param level: initialize the level of the logger, defaults to
            `NOTSET`
        :type level: int or str
        """

        # Call super class
        super().__init__(name=name, level=level)

        # Initialize handler
        # self._initialize_handler()

    def _initialize_configuration(
        self,
    ) -> None:
        """Initialize Configuration for Logger

        Initialize the `default` configuration for the logger. The
        `default` initial configuration is set by the `default.json`
        file in the `configuration` directory.
        """
        ...

    # def _initialize_handler(self) -> None:
    #     """Initialize Handler for Logger

    #     Initialize the Handler for both `stdout` and `stderr`. By
    #     default, `DEBUG`, `INFO`, and `WARNING` will be logged to
    #     `stdout`, while `ERROR` and `CRITICAL` will be logged to
    #     `stderr`.
    #     """

    #     # Initialize `stdout` handler
    #     self.stdout_handler = logging.StreamHandler(sys.stdout)
    #     self.stdout_handler.set_name('stdout-handler')
    #     self.stdout_handler.setLevel(DEBUG)
    #     self.stdout_handler.addFilter(lambda record: record.levelno < ERROR)
    #     self.stdout_handler.setFormatter(LoggerFormatter())
    #     self.addHandler(self.stdout_handler)

    #     # Initialize `stderr` handler
    #     self.stderr_handler = logging.StreamHandler()
    #     self.stderr_handler.set_name('stderr-handler')
    #     self.stderr_handler.setLevel(ERROR)
    #     self.stderr_handler.addFilter(lambda record: record.levelno >= ERROR)
    #     self.stderr_handler.setFormatter(LoggerFormatter())
    #     self.addHandler(self.stderr_handler)

    # def set_formatter(
    #     self,
    #     record_format: str = DEFAULT_RECORD_FORMAT,
    #     date_format: str = DEFAULT_DATE_FORMAT
    # ) -> None:
    #     """Set Formatter for Logger

    #     Enable user to set a different format for the log record and the
    #     log date.

    #     :param record_format: the new format for the log record,
    #         defaults to `RECORD_FORMAT` constant
    #     :type record_format: str
    #     :param date_format: the new format for the log date, defaults to
    #         `DATE_FORMAT` constant
    #     :type date_format: str
    #     """

    #     self.handlers.clear()

    #     # Set formatter for `stdout` handler
    #     self.stdout_handler.setFormatter(
    #         LoggerFormatter(
    #             record_format=record_format,
    #             date_format=date_format
    #         )
    #     )
    #     self.addHandler(self.stdout_handler)

    #     # Set formatter for `stderr` handler
    #     self.stderr_handler.setFormatter(
    #         LoggerFormatter(
    #             record_format=record_format,
    #             date_format=date_format
    #         )
    #     )
    #     self.addHandler(self.stderr_handler)


tealogger = TeaLogger('tealogger')


def critical(
    message: str,
    *args,
    **kwargs
):
    """Log `message` with severity `CRITICAL` level.

    :param message: the message to log
    :type message: str
    """
    tealogger.critical(message, *args, **kwargs)


def error(
    message: str,
    *args,
    **kwargs
):
    """Log `message` with severity `ERROR` level.

    :param message: the message to log
    :type message: str
    """
    tealogger.error(message, *args, **kwargs)


def warning(
    message: str,
    *args,
    **kwargs
):
    """Log `message` with severity `WARNING` level.

    :param message: the message to log
    :type message: str
    """
    tealogger.warning(message, *args, **kwargs)


def info(
    message: str,
    *args,
    **kwargs
):
    """Log `message` with severity `INFO` level.

    :param message: the message to log
    :type message: str
    """
    tealogger.info(message, *args, **kwargs)


def debug(
    message: str,
    *args,
    **kwargs
):
    """Log `message` with severity `DEBUG` level.

    :param message: the message to log
    :type message: str
    """
    tealogger.debug(message, *args, **kwargs)


def log(
    level,
    message: str,
    *args,
    **kwargs
):
    """Log `message` with give `level` severity.

    :param level: the severity level for the log
    :type level: int, use predefined log level
    :param message: the message to log
    :type message: str
    """
    tealogger.log(level, message, *args, **kwargs)
