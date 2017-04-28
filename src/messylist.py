"""Module level docstring."""

import re

class MessyList(object):
    """MessyList object."""
    def __init__(self, filepath):
        """Docstring."""
        with open(filepath) as file_obj:
            self.words = file_obj.read().split()
            self.regex_not_letts = re.compile(r'[^a-zA-Z]')
            self.regex_not_nums = re.compile(r'[^0-9-]')
            self.regex_letts = re.compile(r'[a-zA-Z]')
            self.regex_nums = re.compile(r'[0-9]')
            self.lett_idx = []
            self.num_idx = []

    def are_letters(self, word):
        """Docstring."""
        return bool(re.search(self.regex_letts, word))

    def clean_up(self):
        """Docstring."""
        for idx, word in enumerate(self.words):
            if self.are_letters(word):
                self.lett_idx.append(idx)
                self.words[idx] = re.sub(self.regex_not_letts, '', word)
            else:
                self.num_idx.append(idx)
                self.words[idx] = re.sub(self.regex_not_nums, '', word)
        return self.words


