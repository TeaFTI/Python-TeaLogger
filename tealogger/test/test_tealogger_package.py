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
        set_name: str,
        get_name: str,
    ):
        """Test tealogger Instance
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
