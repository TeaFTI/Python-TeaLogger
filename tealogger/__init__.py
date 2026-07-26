"""
Tea Logger Package
~~~~~~~~~~~~~~~~~~

Tea Logger is a simple logging package for Python.
"""

# Class
# Level
# Function
from .tealogger import (
    CRITICAL,
    DEBUG,
    ERROR,
    INFO,
    NOTSET,
    WARNING,
    TeaLogger,
    configure,
    critical,
    debug,
    error,
    get_logger,
    getLogger,
    info,
    log,
    set_level,
    setLevel,
    warning,
)

__all__ = [
    # Class
    "TeaLogger",
    # Level
    "DEBUG",
    "INFO",
    "WARNING",
    "ERROR",
    "CRITICAL",
    "NOTSET",
    # Function
    "configure",
    "get_logger",
    "getLogger",
    "set_level",
    "setLevel",
    "log",
    "debug",
    "info",
    "warning",
    "error",
    "critical",
]
