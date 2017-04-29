"""
Messylist is a module takes a list of strings containing integers and words and returns a sorted
version of the list. The goal is to sort this list in such a way that all words are in alphabetical
order and all integers are in numerical order. Furthermore, if the nth element in the list is an
integer it must remain an integer, and if it is a word it must remain a word.

In addition, the strings and integers may contain characters that are ascii symbols that neither
belong to letter set nor digit set (i.e. "#", "%", ";", etc). You are required to remove them
during the process so that the output will contain only letters or digits. For example, if a
string is "sym*bo+l", the output should be "symbol". If an integer is "12%3", the output should be
"123". You don't have to worry about strings or integers that contain only non-letter-non-digit
characters, like "^!?", "&", etc.
"""

import re
import sys

class MessyList(object):
    """MessyList type contains methods to perform messy-sort, see module docstring."""
    def __init__(self, filepath):
        """Constructor"""
        with open(filepath) as file_obj:
            self.words = file_obj.read().split()
        self.regex_not_letts = re.compile(r'[^a-zA-Z]')
        self.regex_not_nums = re.compile(r'[^0-9-]')
        self.regex_letts = re.compile(r'[a-zA-Z]')
        self.regex_nums = re.compile(r'[0-9]')
        self.lett_idx = []
        self.num_idx = []

    def are_letters(self, word):
        """Detects whether or not the is letters (versus numbers)."""
        return bool(re.search(self.regex_letts, word))

    def clean_up(self):
        """Remove non-letter and non-number characters from all words."""
        for idx, word in enumerate(self.words):
            if self.are_letters(word):
                self.lett_idx.append(idx)
                self.words[idx] = re.sub(self.regex_not_letts, '', word)
            else:
                self.num_idx.append(idx)
                self.words[idx] = re.sub(self.regex_not_nums, '', word)
        return self.words

    def sorted_letters(self):
        """Alphabetically sort words that are messy letters."""
        return sorted([self.words[i] for i in self.lett_idx])

    def sorted_numbers(self):
        """Numerically sort words that are messy ints."""
        return sorted([int(self.words[i]) for i in self.num_idx])

    def full_sort(self):
        """Implementation of messysort."""
        self.clean_up()
        letts = self.sorted_letters()[::-1]
        nums = self.sorted_numbers()[::-1]
        for idx in self.lett_idx:
            self.words[idx] = letts.pop()
        for idx in self.num_idx:
            self.words[idx] = nums.pop()
        return self.words

    def write_output(self, filepath):
        """Write output file."""
        with open(filepath, mode='w', encoding='utf-8') as myfile:
            for word in self.words:
                myfile.write(str(word) + ' ')
            myfile.truncate(myfile.tell()-1)

    def messy_sort(self, filepath):
        """Sort and write output."""
        self.full_sort()
        self.write_output(filepath)

if __name__ == '__main__':
    MESSY_LIST = MessyList(sys.argv[1])
    MESSY_LIST.messy_sort(sys.argv[2])
