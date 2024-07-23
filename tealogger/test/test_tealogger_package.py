"""
Test Tea Logger Package
~~~~~~~~~~~~~~~~~~~~~~~

This module test functionality for the Tea Logger Package.
"""

import tealogger


class TestTeaLoggerPackage:
    """Test Tea Logger Package"""

    def test_tealogger_instance(
        self,
    ):
        """Test tealogger Instance"""

        tealogger_first = tealogger.TeaLogger('alpha')
        tealogger_second = tealogger.TeaLogger('alpha')

        print(hex(id(tealogger_first)))
        print(hex(id(tealogger_second)))

        assert tealogger_first == tealogger_second

    def test_tealogger_import(
        self,
        attribute: str,
    ):
        """Test tealogger Construction"""

        tealogger.log(tealogger.DEBUG, 'TeaLogger: Debug Message')
        tealogger.debug('TeaLogger: Debug Message')
        tealogger.info('TeaLogger: Info Message')
        tealogger.warning('TeaLogger: Warning Message')
        tealogger.error('TeaLogger: Error Message')
        tealogger.critical('TeaLogger: Critical Message')

        assert hasattr(tealogger, attribute)

    # def test_debug_log(
    #     self,
    #     attribute: str,
    # ):
    #     """Test Debug Log"""

    #     # Set the logging level to DEBUG
    #     tealogger.setLevel(tealogger.DEBUG)

    #     tealogger.debug('TeaLogger: Debug Message')
    #     tealogger.info('TeaLogger: Info Message')
    #     tealogger.warning('TeaLogger: Warning Message')
    #     tealogger.error('TeaLogger: Error Message')
    #     tealogger.critical('TeaLogger: Critical Message')

    #     assert hasattr(tealogger, attribute)
