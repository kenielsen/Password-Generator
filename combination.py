"""
File: combination.py
Author: Kristen Nielsen
Date: 1/2/2018
Description: A class to generation a random combination of a given length
             with the specified separator
"""
from random import randint
from word_choice import WordChoice

class Combination:
    def __init__(self, existing = []):
        """
            Creates a Combination from an existing list.
            existing: List where first item is the separator and the rest
                      will be turned into WordChoice entries.
        """
        self.separator = ""
        self.combination = [] # List of WordChoice
        if existing and len(existing) > 0:
            for itm in existing:
                if "," not in itm:
                    self.separator = itm
                else:
                    itm = itm.split(",")
                    self.combination.append(WordChoice(int(itm[0]), int(itm[1])))
                    
    def generate(self, length=3, words=[]):
        """
            Generates a new combination of the specified length
        """
        while len(self.combination) < length:
            choice = WordChoice()
            choice.widx = randint(1, len(words)) - 1
            choice.cidx = randint(1, words[choice.widx]) - 1
            if choice not in self.combination:
                self.combination.append(choice)
    
    def display(self, words):
        """
            Displays the combination as words with specific letter capitalized
            and separated by separator.
            word_list: List of words to use for this combination.
        """
        combo = []
        for item in self.combination:
            word = words[item.widx]
            idx = item.cidx
            word = word[:idx] + word[idx].upper() + word[idx + 1:]
            combo.append(word)
        return self.separator.join(combo)
    
    def mask(self, words):
        """
            Returns a string with the first and last letters of the passphrase
            separated by '*' to show the length
        """
        combo = self.display(words)
        filler = (len(combo)-1) * '*'
        return combo[0] + filler + combo[-1]

    def hide(self):
        """
            Returns a string of <word index>,<capitalization index>
            separated by <separator> for each WordChoice in combinations
        """
        combo = []
        for item in self.combination:
            combo.append(str(item))
        return self.separator.join(combo)
    
    def __eq__(self, other):
        """ Tests if this Combination is equal to another """
        if not isinstance(other,Combination):
            return False
        if self.separator != other.separator:
            return False
        elif len(self.combination) != len(other.combination):
            return False
        else:
            for i in range(len(self.combination)):
                if self.combination[i] != other.combination[i]:
                    return False
            return True

    def __str__(self):
        rtn = [self.separator]
        for itm in self.combination:
            item = str(itm)
            rtn.append(str(itm))
        return ';'.join(rtn)

    def __len__(self):
        return len(self.combination)
    
    __repr__ = __str__
