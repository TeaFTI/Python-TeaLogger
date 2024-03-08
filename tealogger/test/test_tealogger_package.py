"""
Test Tea Logger Package
~~~~~~~~~~~~~~~~~~~~~~~

This module test functionality for the Tea Logger Package.
"""

import tealogger

class TestTeaLoggerPackage:
    """Test Tea Logger Package"""

    def test_base_import(
        self,
    ):
        """Test Base Construction"""

        tealogger.debug('TeaLogger: Debug Message')
        tealogger.info('TeaLogger: Info Message')
        tealogger.warning('TeaLogger: Warning Message')
        tealogger.error('TeaLogger: Error Message')
        tealogger.critical('TeaLogger: Critical Message')


    def test_debug_log(
        self,
    ):
        """Test Debug Log"""

        # Set the logging level to DEBUG
        tealogger.setLevel(tealogger.DEBUG)

        tealogger.debug('TeaLogger: Debug Message')
        tealogger.info('TeaLogger: Info Message')
        tealogger.warning('TeaLogger: Warning Message')
        tealogger.error('TeaLogger: Error Message')
        tealogger.critical('TeaLogger: Critical Message')
