"""Module level docstring."""

class MessyList(object):
    """MessyList object."""
    def __init__(self, filepath):
        with open(filepath) as file_obj:
            self.words = file_obj.read().split()
