"""
File: word_choice.py
Author: Kristen Nielsen
Date: 1/2/2018
Description: A class to hold the combination of word index and what letter
             gets capitalized in the word
"""
class WordChoice:
    def __init__(self, word_index = None, cap_index = None):
        """
            Creates a WordChoice with the given word index and capitalization
            index.
        """
        self.widx = word_index
        self.cidx = cap_index

    def __eq__(self, other):
        if not isinstance(other, WordChoice):
            return False
        else:
            return self.widx == other.widx

    def __str__(self):
        return str(self.widx) + ',' + str(self.cidx)

    __repr__ = __str__
