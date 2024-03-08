"""
Test Tea Logger Module
~~~~~~~~~~~~~~~~~~~~~~

This module test functionality for the TeaLogger.
"""

import logging

import tealogger

class TestTeaLogger:
    """Test Tea Logger"""

    def test_base_construction(self):
        """Test Base Construction"""

        base = tealogger.TeaLogger(
            name='base',
            level=tealogger.DEBUG
        )

        base.debug('TeaLogger: Debug Message')
        base.info('TeaLogger: Info Message')
        base.warning('TeaLogger: Warning Message')
        base.error('TeaLogger: Error Message')
        base.critical('TeaLogger: Critical Message')

