"""
Test Tea Logger Package
~~~~~~~~~~~~~~~~~~~~~~~

This module test functionality for the Tea Logger Package.
"""

import pytest

import tealogger

class TestTeaLoggerPackage:
    """Test Tea Logger Package"""

    @pytest.mark.parametrize(
        'attribute',
        [
            ('setLevel'),
        ]
    )
    def test_tealogger_import(
        self,
        attribute: str,
    ):
        """Test tealogger Construction"""

        tealogger.debug('TeaLogger: Debug Message')
        tealogger.info('TeaLogger: Info Message')
        tealogger.warning('TeaLogger: Warning Message')
        tealogger.error('TeaLogger: Error Message')
        tealogger.critical('TeaLogger: Critical Message')

        assert hasattr(tealogger, attribute)


    @pytest.mark.parametrize(
        'attribute',
        [
            ('log'),
        ]
    )
    def test_debug_log(
        self,
        attribute: str,
    ):
        """Test Debug Log"""

        # Set the logging level to DEBUG
        tealogger.setLevel(tealogger.DEBUG)

        tealogger.debug('TeaLogger: Debug Message')
        tealogger.info('TeaLogger: Info Message')
        tealogger.warning('TeaLogger: Warning Message')
        tealogger.error('TeaLogger: Error Message')
        tealogger.critical('TeaLogger: Critical Message')

        assert hasattr(tealogger, attribute)
