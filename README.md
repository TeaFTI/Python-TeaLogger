# Tea Logger

Python Tea Logger

## Table of Content
* [Note](#note)
* [Reference](#reference)

## Overview

### Level

From high (`CRITICAL`) to low (`DEBUG`).

* `CRITICAL` = 50
* `FATAL` = `CRITICAL` (Do not use, use `CRITICAL` instead)
* `ERROR` = 40
* `WARNING` = 30
* `WARN` = `WARNING` (Deprecated, use `WARNING` instead)
* `INFO` = 20
* `DEBUG` = 10
* `NOTSET` = 0
* `EXCEPTION`

## Note

### Child Logger

When creating a child logger, if there are no handler(s) added, it will
inherit the handle(s) from the parent. But if the parent logger itself
is set to a higher level, the higher level gets respected. Since the
parent handler(s) attached to the parent logger only output if the
parent logger allows it.

## Reference

* [logging - Logging facility for Python](https://docs.python.org/3/library/logging.html)
* [Logging HOWTO](https://docs.python.org/3/howto/logging.html)
* [Logging Cookbook](https://docs.python.org/3/howto/logging-cookbook.html)
