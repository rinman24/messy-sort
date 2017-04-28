import os
from src.messylist import MessyList

TESTDATA_FILENAME_01 = os.path.join(os.path.dirname(__file__), 'test_input/test01.txt')

class TestReadInput:
    """Testing MessyList type for ability to read files."""
    def test_read_input01(self):
        """Read in a basic file."""
        messy_list = MessyList(TESTDATA_FILENAME_01)
        assert messy_list.words == ['start', '-102', 'finish', '992484', 'bi$d', '&-?24#']
