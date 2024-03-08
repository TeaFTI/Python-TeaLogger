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

        tea_logger = tealogger.TeaLogger(
            name='base',
            level=tealogger.DEBUG
        )

        tea_logger.debug('TeaLogger: Debug Message')
        tea_logger.info('TeaLogger: Info Message')
        tea_logger.warning('TeaLogger: Warning Message')
        tea_logger.error('TeaLogger: Error Message')
        tea_logger.critical('TeaLogger: Critical Message')

