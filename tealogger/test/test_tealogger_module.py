"""
Test Tea Logger Module
~~~~~~~~~~~~~~~~~~~~~~

This module test functionality for the TeaLogger.
"""

import logging
from typing import Union

import pytest

import tealogger

class TestTeaLogger:
    """Test Tea Logger"""

    @pytest.mark.parametrize(
        'name, level, expected',
        [
            (None, tealogger.DEBUG, logging.Logger),
            ('base', tealogger.DEBUG, logging.Logger),
        ]
    )
    def test_base_construction(
        self,
        name: Union[str, None],
        level: Union[int, str],
        expected,
    ):
        """Test Base Construction"""

        base = tealogger.TeaLogger(
            name=name,
            level=level
        )

        base.debug('TeaLogger: Debug Message')
        base.info('TeaLogger: Info Message')
        base.warning('TeaLogger: Warning Message')
        base.error('TeaLogger: Error Message')
        base.critical('TeaLogger: Critical Message')

        assert isinstance(base, expected)
