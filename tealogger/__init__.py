"""
Tea Logger Package
~~~~~~~~~~~~~~~~~~

Tea Logger is a simple logging package for Python.
"""

from typing import Union

from tealogger.tealogger import (
    TeaLogger
)

from tealogger.tealogger import (
    DEBUG,
    INFO,
    WARNING,
    ERROR,
    CRITICAL,
    NOTSET
)


tea = TeaLogger(
    name=__name__,
    level=WARNING
)


def set_level(
    level: Union[int, str] = NOTSET,
):
    """Set the logging level of the Tea Logger (Package).

    :param level: The level for the TeaLogger, defaults to NOTSET
    :type level: int or str, optional
    """
    tea.setLevel(level)


# Alias
setLevel = set_level


def log(
    level,
    message: str,
    *args,
    **kwargs
):
    """Log message with give level severity.

    :param level: The severity level for the log
    :type level: int, use predefined log level
    :param message: The message to log
    :type message: str
    """
    tea.log(level, message, *args, **kwargs)


def debug(
    message: str,
    *args,
    **kwargs
):
    """Log message with severity DEBUG level.

    :param message: The message to log
    :type message: str
    """
    tea.debug(message, *args, **kwargs)


def info(
    message: str,
    *args,
    **kwargs
):
    """Log message with severity INFO level.

    :param message: The message to log
    :type message: str
    """
    tea.info(message, *args, **kwargs)


def warning(
    message: str,
    *args,
    **kwargs
):
    """Log message with severity WARNING level.

    :param message: The message to log
    :type message: str
    """
    tea.warning(message, *args, **kwargs)


def error(
    message: str,
    *args,
    **kwargs
):
    """Log message with severity ERROR level.

    :param message: The message to log
    :type message: str
    """
    tea.error(message, *args, **kwargs)


def critical(
    message: str,
    *args,
    **kwargs
):
    """Log message with severity CRITICAL level.

    :param message: The message to log
    :type message: str
    """
    tea.critical(message, *args, **kwargs)
