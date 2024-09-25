"""
Test Pytest
~~~~~~~~~~~

This module test functionality of Tea Logger with Pytest.
"""

import tealogger
from tealogger import TeaLogger

class TestClass:
    """Test Class"""

    def test_class_instance(
        self,
        set_name: str,
        get_name: str,
    ):
        """Test Class Instance

        Test the import of the Tealogger class, and the create of a new
        instance of the TeaLogger class.

        :param set_name: The name of the new TeaLogger instance to set
        :type set_name: str
        :param get_name: The name of the new TeaLogger instance to get
        :type get_name: str
        """

        tealogger_set = TeaLogger(set_name)
        tealogger_get = TeaLogger(get_name)

        tealogger_set_id = hex(id(tealogger_set))
        tealogger_get_id = hex(id(tealogger_get))

        tealogger.debug('TeaLogger First Hex ID: %s', tealogger_set_id)
        tealogger.debug('TeaLogger Second Hex ID: %s', tealogger_get_id)

        # Standard compare
        assert tealogger_set == tealogger_get
        # Identity compare
        assert tealogger_set is tealogger_get
