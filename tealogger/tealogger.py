"""
Tea Logger Module
~~~~~~~~~~~~~~~~~

The module implements the core functionality of the Tea Logger.
"""

import json
import logging
import logging.config
from pathlib import Path
from typing import Union


# Log Level
CRITICAL = logging.CRITICAL
FATAL = logging.FATAL
ERROR = logging.ERROR
WARNING = logging.WARNING
WARN = logging.WARN
INFO = logging.INFO
DEBUG = logging.DEBUG
NOTSET = logging.NOTSET

ESC = '\x1b['

_COLOR_CODE = {
    # Reset
    'RESET': f'{ESC}0m',
    # Foreground
    'FOREGROUND_BLACK': f'{ESC}30m',
    'FOREGROUND_RED': f'{ESC}31m',
    'FOREGROUND_GREEN': f'{ESC}32m',
    'FOREGROUND_YELLOW': f'{ESC}33m',
    'FOREGROUND_BLUE': f'{ESC}34m',
    'FOREGROUND_MAGENTA': f'{ESC}35m',
    'FOREGROUND_CYAN': f'{ESC}36m',
    'FOREGROUND_WHITE': f'{ESC}37m',
    'FOREGROUND_DEFAULT': f'{ESC}39m',
    # Background
    'BACKGROUND_BLACK': f'{ESC}40m',
    'BACKGROUND_RED': f'{ESC}41m',
    'BACKGROUND_GREEN': f'{ESC}42m',
    'BACKGROUND_YELLOW': f'{ESC}43m',
    'BACKGROUND_BLUE': f'{ESC}44m',
    'BACKGROUND_MAGENTA': f'{ESC}45m',
    'BACKGROUND_CYAN': f'{ESC}46m',
    'BACKGROUND_WHITE': f'{ESC}47m',
    'BACKGROUND_DEFAULT': f'{ESC}49m',
    # Style
    'STYLE_BOLD': f'{ESC}1m',
    'STYLE_DIM': f'{ESC}2m',
    'STYLE_UNDERLINED': f'{ESC}4m',
    'STYLE_BLINK': f'{ESC}5m',
    'STYLE_REVERSE': f'{ESC}7m',
    'STYLE_HIDDEN': f'{ESC}8m',
    'STYLE_DEFAULT': f'{ESC}22m',
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


class ColorFormatter(logging.Formatter):
    """Color Formatter

    Define a color Formatter.
    """

    def __init__(
        self,
        record_format: Union[str, None] = None,
        date_format: Union[str, None] = None
    ) -> None:
        """Initialize Constructor

        :param record_format: The record format for the Formatter,
            defaults to None, set from configuration
        :type record_format: str, optional
        :param date_format: The date format for the Formatter, defaults
            to None, set from configuration
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

        self._date_format = date_format

    def format(
        self,
        record: logging.LogRecord
    ) -> str:
        """Format the specified record as text (redefined)

        :param record: The record to format, used for string formatting
            operation
        :type record: dict

        :return: The formatted record
        :rtype: str
        """
        log_format = self._level_format.get(record.levelno)
        formatter = logging.Formatter(
            fmt=log_format,
            datefmt=self._date_format
        )

        return formatter.format(record)


class StandardSteamHandler(logging.StreamHandler):
    """Standard Steam Handler"""


class StandardOutFilter(logging.Filter):
    """Standard Out Filter"""

    def filter(self, record: logging.LogRecord) -> bool:
        """Filter the specified record

        Determine if the specified record is to be logged.

        :param record: The record to filter
        :type record: dict

        :return: Whether or not the record should be logged
        :rtype: bool
        """

        return record.levelno <= WARNING


class TeaLogger(logging.Logger):
    """Tea Logger"""

    def __new__(
        cls,
        name: Union[str, None] = None,
        level: Union[int, str] = NOTSET,
        **kwargs
    ):
        """Create Constructor

        Create new instance of the TeaLogger class.

        :param name: The name for the TeaLogger, defaults to None
        :type name: str or None, optional
        :param level: The level for the TeaLogger, defaults to NOTSET
        :type level: int or str, optional
        :param dictConfig: The dictionary configuration for the
            TeaLogger, defaults to None
        :type dictConfig: dict, optional
        :param fileConfig: The file configuration for the TeaLogger,
            defaults to None
        :type fileConfig: str, optional

        :return: The new instance of TeaLogger class (Self)
        :rtype: TeaLogger
        """

        # Get (Create) the Logger
        tea = logging.getLogger(name)

        # Configuration
        if kwargs.get('dictConfig'):
            # Dictionary
            logging.config.dictConfig(kwargs.get('dictConfig'))
        elif kwargs.get('fileConfig'):
            # File
            ...
        else:
            # Default
            current_module_path = Path(__file__).parent.expanduser().resolve()
            with open(
                current_module_path / 'configuration' / 'default.json',
                mode='r',
                encoding='utf-8'
            ) as file:
                configuration = json.load(file)

            if 'loggers' not in configuration:
                configuration['loggers'] = {}
            elif name not in configuration['loggers']:
                configuration['loggers'][name] = {}

            # NOTE: Override only individual configuration!
            # Overriding the entire configuration will cause this child
            # logger to inherit any missing configuration from the root
            # logger. (Even if the configuration was set previously.)
            configuration['loggers'][name]['level'] = logging.getLevelName(level)

            logging.config.dictConfig(configuration)

        return tea

    def __init__(
        self,
        name: str,
        level: Union[int, str] = NOTSET
    ) -> None:
        """Initialize Constructor

        Initialize the instance of the TeaLogger class.

        :param name: The name for the TeaLogger
        :type name: str
        :param level: The level for the TeaLogger, defaults to NOTSET
        :type level: int or str, optional
        :return: The new instance of TeaLogger class (Self)
        :rtype: TeaLogger
        """
        # Call super class
        super().__init__(name=name, level=level)
