"""
Test Package
~~~~~~~~~~~~

This module test functionality for the Tea Logger Package.
"""

from collections.abc import Generator

from pytest import CaptureFixture
import tealogger


class TestPackage:
    """Test Package"""

    def test_instance(
        self,
        set_name: str,
        get_name: str,
    ):
        """Test Instance

        Test the create of a new instance of the TeaLogger class.

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
        capfd: Generator[CaptureFixture[str], None, None],
        # caplog: Generator[LogCaptureFixture, None, None],
    ):
        """Test Debug Log"""

        # Set the logging level to level
        tealogger.setLevel(level)

        # tealogger.log(level, message)
        tealogger.debug('Debug Message')
        tealogger.info('Info Message')
        tealogger.warning('Warning Message')
        tealogger.error('Error Message')
        tealogger.critical('Critical Message')

        # Get
        # - Standard Output (file descriptor 1)
        # - Standard Error (file descriptor 2)
        stdout, _ = capfd.readouterr()
        # print(repr(stdout))

        assert message in stdout
