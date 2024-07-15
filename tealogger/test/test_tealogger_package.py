"""
Test Tea Logger Package
~~~~~~~~~~~~~~~~~~~~~~~

This module test functionality for the Tea Logger Package.
"""

import tealogger


class TestTeaLoggerPackage:
    """Test Tea Logger Package"""

    # def test_tealogger_instance(
    #     self,
    # ):
    #     """Test Tea Logger Instance"""

    #     tealogger_a1 = tealogger.TeaLogger('Alpha')
    #     tealogger_a2 = tealogger.TeaLogger('Alpha')

    #     print(hex(id(tealogger_a1)))
    #     print(hex(id(tealogger_a2)))

    #     assert tealogger_a1 == tealogger_a2

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
