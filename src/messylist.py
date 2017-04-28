"""Module level docstring."""

import re
import sys

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

    def sorted_letters(self):
        """Docstring."""
        return sorted([self.words[i] for i in self.lett_idx])

    def sorted_numbers(self):
        """Docstring."""
        return sorted([int(self.words[i]) for i in self.num_idx])

    def full_sort(self):
        """Docstring."""
        self.clean_up()
        letts = self.sorted_letters()[::-1]
        nums = self.sorted_numbers()[::-1]
        for idx in self.lett_idx:
            self.words[idx] = letts.pop()
        for idx in self.num_idx:
            self.words[idx] = nums.pop()
        return self.words

    def write_output(self, filepath):
        """Docstring."""
        with open(filepath, mode='w', encoding='utf-8') as myfile:
            for word in self.words:
                myfile.write(str(word) + ' ')
            myfile.truncate(myfile.tell()-1)

    def messy_sort(self, filepath):
    	"""Docstring."""
    	self.full_sort()
    	self.write_output(filepath)

if __name__ == '__main__':
    messy_list = MessyList(sys.argv[1])
    messy_list.messy_sort(sys.argv[2])








