"""
Test Package
~~~~~~~~~~~~

This module test functionality for the Tea Logger Package.
"""

from collections.abc import Generator
import json
from pathlib import Path

# from pytest import CaptureFixture
from pytest import LogCaptureFixture

import tealogger


class TestPackage:
    """Test Package"""

    def test_instance(
        self,
        set_name: str,
        get_name: str,
    ):
        """Test Instance

        Test the import of the tealogger package, and the create of a
        new instance of the TeaLogger class.

        :param set_name: The name of the new TeaLogger instance to set
        :type set_name: str
        :param get_name: The name of the new TeaLogger instance to get
        :type get_name: str
        """

        tealogger_set = tealogger.TeaLogger(set_name)
        tealogger_get = tealogger.TeaLogger(get_name)

        tealogger_set_id = hex(id(tealogger_set))
        tealogger_get_id = hex(id(tealogger_get))

        tealogger.debug('TeaLogger First Hex ID: %s', tealogger_set_id)
        tealogger.debug('TeaLogger Second Hex ID: %s', tealogger_get_id)

        # Standard compare
        assert tealogger_set == tealogger_get
        # Identity compare
        assert tealogger_set is tealogger_get

    def test_import(
        self,
        attribute: str,
    ):
        """Test Construction

        Test the construction and import attribute of the TeaLogger
        class.

        :param attribute: The attribute of the TeaLogger object
        :type attribute: str
        """

        tealogger.log(tealogger.DEBUG, 'TeaLogger: Debug Message')
        tealogger.debug('TeaLogger: Debug Message')
        tealogger.info('TeaLogger: Info Message')
        tealogger.warning('TeaLogger: Warning Message')
        tealogger.error('TeaLogger: Error Message')
        tealogger.critical('TeaLogger: Critical Message')

        assert hasattr(tealogger, attribute)

    def test_str_level(
        self,
        level: str,
        message: str,
        # capfd: Generator[CaptureFixture[str], None, None],
        caplog: Generator[LogCaptureFixture, None, None],
    ):
        """Test String Level Log

        Test the logging of a message with a string level. Use caplog to
        capture the output, and validate the message is in the output.

        :param level: The level to set the logger
        :type level: str
        :param message: The message to log
        :type message: str
        :param caplog: The log capture fixture
        :type caplog: Generator[LogCaptureFixture, None, None]

        NOTE: This is not the best test implementation, but it works
        cross-platform. The capfd for some reason have issue working on
        Windows.
        """

        level_logger_name = 'tealogger.test.package.level'

        level_logger = tealogger.get_logger(name=level_logger_name)

        # Set the logging level to level
        level_logger.setLevel(level)

        with caplog.at_level(level, logger=level_logger_name):
            level_logger.debug('Debug Message')
            level_logger.info('Info Message')
            level_logger.warning('Warning Message')
            level_logger.error('Error Message')
            level_logger.critical('Critical Message')

        # print("Record: ", caplog.records)
        # print("Record Text: ", caplog.text)

        # Get
        # - Standard Output (file descriptor 1)
        # - Standard Error (file descriptor 2)
        # stdout, _ = capfd.readouterr()
        # print(repr(stdout))

        # assert message in stdout
        assert message in caplog.text

    def test_dict_config(
        self,
    ):
        """Test Dictionary Configuration

        Test the construction of TeaLogger with a dictionary
        configuration via JSON (JavaScript Object Notation).
        """

        dict_config_logger_name = 'tealogger.test.package.dictconfig'

        configuration = None
        current_module_path = Path(__file__).parent.expanduser().resolve()
        with open(
            current_module_path / 'tealogger.json',
            mode='r',
            encoding='utf-8'
        ) as file:
            configuration = json.load(file)

        dict_config_logger = tealogger.TeaLogger(
            dict_config_logger_name,
            dictConfig=configuration
        )

        assert dict_config_logger.name == dict_config_logger_name
