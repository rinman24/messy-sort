import os
from src.messylist import MessyList

DIRNAME = os.path.dirname(__file__)
TESTDATA_FILENAME_01 = os.path.join(DIRNAME, 'test_input/test01.txt')
BLANKDATA = os.path.join(DIRNAME, 'test_input/test_blank.txt')
SPACEDATA = os.path.join(DIRNAME, 'test_input/test_spaces.txt')
NEWLINE_DATA = os.path.join(os.path.dirname(__file__), 'test_input/test_newline.txt')
LEADING_WHITESPACE = os.path.join(os.path.dirname(__file__), 'test_input/test_leading_whitespace.txt')
TRAILING_WHITESPACE = os.path.join(os.path.dirname(__file__), 'test_input/test_trailing_whitespace.txt')
WHITESPACE_BETWEEN = os.path.join(os.path.dirname(__file__), 'test_input/test_whitespace_between.txt')

class TestReadInput:
    """Testing MessyList type for ability to read files."""
    truth_list = ['start', '-102', 'finish', '992484', 'bi$d', '&-?24#']

    def test_read_input01(self):
        """Read in a basic file."""
        messy_list = MessyList(TESTDATA_FILENAME_01)
        assert messy_list.words == self.truth_list

    def test_read_blank_data(self):
        """Read in blank data file."""
        messy_list = MessyList(BLANKDATA)
        assert messy_list.words == []

    def test_read_spaces(self):
        """Read in several spaces."""
        messy_list = MessyList(SPACEDATA)
        assert messy_list.words == []

    def test_read_new_line(self):
        """Read in a file with a newline."""
        messy_list = MessyList(NEWLINE_DATA)
        assert messy_list.words == self.truth_list

    def test_read_leading_whitespace(self):
        """Read in a file with leading whitespace"""
        messy_list = MessyList(LEADING_WHITESPACE)
        assert messy_list.words == self.truth_list

    def test_read_trailing_whitespace(self):
        """Read in a file with trailing whitespace"""
        messy_list = MessyList(TRAILING_WHITESPACE)
        assert messy_list.words == self.truth_list

    def test_read_whitespace_between(self):
        """Read in a file with extra whitespace between words"""
        messy_list = MessyList(WHITESPACE_BETWEEN)
        assert messy_list.words == self.truth_list

