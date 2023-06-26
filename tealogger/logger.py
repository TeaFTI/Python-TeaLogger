"""Logger Module

This module implements the Tea Logger.
"""

import logging
from logging import LogRecord
import sys


# Log Level
CRITICAL = logging.CRITICAL
FATAL = logging.FATAL
ERROR = logging.ERROR
WARNING = logging.WARNING
WARN = logging.WARN
INFO = logging.INFO
DEBUG = logging.DEBUG
NOTSET = logging.NOTSET

RECORD_FORMAT = '[%(name)s %(levelname)s %(asctime)s] %(message)s'
DATE_FORMAT = '%Y-%m-%d %H:%M:%S'


class ColorCode:
    """Color Code for logging"""

    # Reset
    RESET = '\x1b[0m'
    # Foreground
    FOREGROUND_BLACK = '\x1b[30m'
    FOREGROUND_RED = '\x1b[31m'
    FOREGROUND_GREEN = '\x1b[32m'
    FOREGROUND_YELLOW = '\x1b[33m'
    FOREGROUND_BLUE = '\x1b[34m'
    FOREGROUND_MAGENTA = '\x1b[35m'
    FOREGROUND_CYAN = '\x1b[36m'
    FOREGROUND_WHITE = '\x1b[37m'
    FOREGROUND_DEFAULT = '\x1b[39m'
    # Background
    BACKGROUND_BLACK = '\x1b[40m'
    BACKGROUND_RED = '\x1b[41m'
    BACKGROUND_GREEN = '\x1b[42m'
    BACKGROUND_YELLOW = '\x1b[43m'
    BACKGROUND_BLUE = '\x1b[44m'
    BACKGROUND_MAGENTA = '\x1b[45m'
    BACKGROUND_CYAN = '\x1b[46m'
    BACKGROUND_WHITE = '\x1b[47m'
    BACKGROUND_DEFAULT = '\x1b[49m'
    # Style
    STYLE_BOLD = '\x1b[1m'
    STYLE_DIM = '\x1b[2m'
    STYLE_UNDERLINED = '\x1b[4m'
    STYLE_BLINK = '\x1b[5m'
    STYLE_REVERSE = '\x1b[7m'
    STYLE_HIDDEN = '\x1b[8m'
    STYLE_DEFAULT = '\x1b[22m'
    
    NOTSET = RESET
    DEBUG = f'{FOREGROUND_CYAN}'
    INFO = f'{FOREGROUND_GREEN}'
    WARNING = f'{FOREGROUND_YELLOW}'
    SUCCESS = f'{FOREGROUND_GREEN}'
    ERROR = f'{FOREGROUND_RED}'
    CRITICAL = f'{FOREGROUND_RED}{BACKGROUND_WHITE}'


class LoggerFormatter(logging.Formatter):
    """Formatter for the Logger

    Define a custom Logger Formatter with color.
    """

    def __init__(
        self,
        record_format: str = RECORD_FORMAT,
        date_format: str = DATE_FORMAT
        ) -> None:
        """Constructor

        :param log_format: (str) the log format for the Formatter
        :param date_format: (str) the date format for the Formatter
        """
        # Call super class
        super().__init__(fmt=record_format, datefmt=date_format)

        self.LEVEL_FORMAT = {
            logging.DEBUG: f'{ColorCode.DEBUG}{record_format}{ColorCode.RESET}',
            logging.INFO: f'{ColorCode.INFO}{record_format}{ColorCode.RESET}',
            logging.WARNING: f'{ColorCode.WARNING}{record_format}{ColorCode.RESET}',
            logging.ERROR: f'{ColorCode.ERROR}{record_format}{ColorCode.RESET}',
            logging.CRITICAL: f'{ColorCode.CRITICAL}{record_format}{ColorCode.RESET}'
            }

        self.date_format = date_format

    
    def format(self, record: LogRecord) -> str:
        """Format the specified record as text (redefined)

        :param record: (dict) the record to format, used for string
            formatting operation

        :return: (str) the formatted record
        """
        log_format = self.LEVEL_FORMAT.get(record.levelno)
        formatter = logging.Formatter(fmt=log_format, datefmt=self.date_format)

        return formatter.format(record)


class Logger(logging.Logger):
    """Logger class for AutoTools

    A Logger with predefined log format.
    """

    def __init__(
        self,
        name: str,
        level=NOTSET
        ) -> None:
        # No UnionType yet
        # level: int | str = NOTSET) -> None:
        """Constructor
        
        :param name: (str) the name of the logger
        :param level: (int) or (str) initialize the level of the logger
        """

        # Call super class
        super(Logger, self).__init__(name=name, level=level)

        # Initialize handler
        self._initialize_handler()


    def _initialize_handler(self) -> None:
        """Initialize Handler for Logger
        
        Initialize the Handler for both `stdout` and `stderr`. By
        default, `DEBUG`, `INFO`, and `WARNING` will be logged to
        `stdout`, while `ERROR` and `CRITICAL` will be logged to
        `stderr`.
        """

        # Initialize `stdout` handler
        self.stdout_handler = logging.StreamHandler(sys.stdout)
        self.stdout_handler.set_name('stdout-handler')
        self.stdout_handler.setLevel(DEBUG)
        self.stdout_handler.addFilter(lambda record: record.levelno < ERROR)
        self.stdout_handler.setFormatter(LoggerFormatter())
        self.addHandler(self.stdout_handler)

        # Initialize `stderr` handler
        self.stderr_handler = logging.StreamHandler()
        self.stderr_handler.set_name('stderr-handler')
        self.stderr_handler.setLevel(ERROR)
        self.stderr_handler.addFilter(lambda record: record.levelno >= ERROR)
        self.stderr_handler.setFormatter(LoggerFormatter())
        self.addHandler(self.stderr_handler)


    def set_formatter(
        self,
        record_format: str = RECORD_FORMAT,
        date_format: str = DATE_FORMAT
        ) -> None:
        """Set Formatter for Logger

        Enable user to set a different format for the log record and the
        log date.

        :param record_format: (str) the new format for the log record
        :param date_format: (str) the new format for the log date
        """

        self.handlers.clear()

        # Set formatter for `stdout` handler
        self.stdout_handler.setFormatter(
            LoggerFormatter(
                record_format=record_format,
                date_format=date_format
                )
            )
        self.addHandler(self.stdout_handler)

        # Set formatter for `stderr` handler
        self.stderr_handler.setFormatter(
            LoggerFormatter(
                record_format=record_format,
                date_format=date_format
                )
            )
        self.addHandler(self.stderr_handler)
