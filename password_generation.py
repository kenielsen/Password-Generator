from combination import Combination


class FileManipulator:
    def __init__(self, filename):
        self._filename = filename

    def read_file_to_list(self, sep = '\n'):
        """ Reads specified file to a list based on separator """
        try:
            f = open(self._filename, 'r')
            lst = f.read().split(sep)
            f.close()
            if lst[-1] == '':
                del lst[-1]
            return lst
        except FileNotFoundException:
            return []

    def count_lines(self):
        """ Counts the number of nonblank lines in a file"""
        num_lines = 0
        with open(self._filename, 'r') as f:
            lines = f.readlines()
            num_lines = len([1 for l in lines if l.strip('\n') != ''])
        return num_lines

    def read_file_to_length_list(self):
        """ Returns a list of the lengths of lines in a file """
        lst = []
        try:
            with open(self._filename, 'r') as f:
                for line in f:
                    if len(line.strip('\n')) > 0:
                        lst.append(len(line.strip('\n')))
            return lst
        except:
            return lst
        return lst

    def write_list_to_file(self, lst):
        with open(self._filename, 'w') as f:
            for line in lst:
                f.write(line + '\n')

    def add_line_to_file(self, line):
        with open(self._filename, 'a') as f:
            f.write(line + '\n')
            

# Global variables
COMBINATION_FILE = "used_combinations.txt"
WORD_FILE = "word_list.txt"

# Combination specific
class CombinationManipulator:
    def __init__(self):
        self._file_manipulator = FileManipulator(COMBINATION_FILE)
        
    def read(self):
        """ Reads COMBINATION_FILE into a list of Combinations."""
        combos = []
        tmp = self._file_manipulator.read_file_to_list()
        for item in tmp:
            combos.append(Combination(item.split(';')))
        return combos

    def count(self):
        """ Returns the number of combinations in COMBINATION_FILE"""
        return self._file_manipulator.count_lines()

    def generate(self,separator = "&", length=3):
        """ Generates a new combination with the given separator and of the given
            length that is currently not in COMBINATION_FILE."""
        combo = Combination()
        combo.separator = separator
        used = self.read()
        
        f = FileManipulator(WORD_FILE)
        words = f.read_file_to_length_list()
        del f
        
        combo.generate(length, words)
        while combo in used:
            combo.generate(separator, length, words)
        
        self._file_manipulator.add_line_to_file(str(combo))
        return combo

    def get(self, index):
        return Combination(self._file_manipulator.read_file_to_list()[index].split(';'))

    def view(self, index):
        f = FileManipulator(WORD_FILE)
        words = f.read_file_to_list()
        del f
        return self.get(index).display(words)

# Word list specific
class WordManipulator:
    def __init__(self):
        self._file_manipulator = FileManipulator(WORD_FILE)
        
    def count(self):
        return self._file_manipulator.count_lines()

    def read(self):
        return self._file_manipulator.read_file_to_list()

    def delete(self, word):
        words = self._file_manipulator.read_file_to_list()
        if isinstance(word, str) and word in words:
            del words[words.index(word)]
        elif isinstance(word, int) and word < len(words) and word >= 0:
            del words[word]
        else: return False
        self._file_manipulator.write_list_to_file(words)
        return True

    def add(self, word):
        words = self._file_manipulator.read_file_to_list()
        if word in words:
            return False
        else:
            self._file_manipulator.add_line_to_file(word)
            return True
