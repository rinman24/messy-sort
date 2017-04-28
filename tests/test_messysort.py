import os
from messylist import MessyList

TESTDATA_FILENAME_01 = os.path.join(os.path.dirname(__file__), 'test_input/test01.txt')

class ReadInput:
    """Docstring."""
    def test_read_input(self):
        """Docstring."""
        print(TESTDATA_FILENAME_01)
        messy_list = MessyList(TESTDATA_FILENAME_01)
