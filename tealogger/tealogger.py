"""Logger Module

This module implements the Tea Logger.
"""

import json
import logging
import logging.config
from pathlib import Path
from typing import (override, Self, Union)


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
    def format(self, record: logging.LogRecord) -> str:
        log_format = self._level_format.get(record.levelno)
        formatter = logging.Formatter(fmt=log_format, datefmt=self.date_format)

        return formatter.format(record)


class TeaLogger(logging.Logger):
    """Tea Logger
    """

    def __new__(
        cls,
        name: str = 'tea',
        level: Union[int, str] = NOTSET,
        **kwargs
    ) -> Self:
        """Create Constructor

        Create new instance of the TeaLogger class.

        :param name: The name for the TeaLogger
        :type name: str
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
            ...
        elif kwargs.get('fileConfig'):
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

            logging.config.dictConfig(configuration)

        return tea

    def __init__(
        self,
        name: str,
        level: Union[int, str] = NOTSET,
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
