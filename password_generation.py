from combination import Combination

def read_file_to_list(filename, sep = '\n'):
    """ Reads specified file to a list based on separator """
    try:
        f = open(filename, 'r')
        lst = f.read().split(sep)
        f.close()
        if lst[-1] == '':
            del lst[-1]
        return lst
    except FileNotFoundException:
        return []

def count_lines(filename):
    """ Counts the number of nonblank lines in a file"""
    num_lines = 0
    with open(filename, 'r') as f:
        lines = f.readlines()
        num_lines = len([1 for l in lines if l.strip('\n') != ''])
    return num_lines

def read_file_to_length_list(filename):
    """ Returns a list of the lengths of lines in a file """
    lst = []
    try:
        with open(filename, 'r') as f:
            for line in f:
                if len(line.strip('\n')) > 0:
                    lst.append(len(line.strip('\n')))
        return lst
    except:
        return lst
    return lst

# Global variables
COMBINATION_FILE = "used_combinations.txt"
WORD_FILE = "word_list.txt"

# Combination specific
def read_combinations():
    """ Reads COMBINATION_FILE into a list of Combinations."""
    combos = []
    tmp = read_file_to_list(COMBINATION_FILE)
    for item in tmp:
        combos.append(Combination(item.split(';')))
    return combos

def count_combos():
    """ Returns the number of combinations in COMBINATION_FILE"""
    return count_lines(COMBINATION_FILE)

def generate_new_combination(separator = "&", length=3):
    """ Generates a new combination with the given separator and of the given
        length that is currently not in COMBINATION_FILE."""
    combo = Combination()
    combo.separator = separator
    used = read_combinations()
    words = read_file_to_length_list(WORD_FILE)
    combo.generate(length, words)
    while combo in used:
        combo.generate(separator, length, words)
    #write c to COMBINATION_FILE
    with open(COMBINATION_FILE, 'a') as f:
        f.write(str(combo) + "\n")
    return combo

def get_combination(index):
    return Combination(read_file_to_list(COMBINATION_FILE)[index].split(';'))

# Word list specific
def count_words():
    return count_lines(WORD_FILE)

def get_words():
    return read_file_to_list(WORD_FILE)

def delete_word(word):
    words = read_file_to_list(WORD_FILE)
    if word in words:
        del words[words.index(word)]
    f = open(WORD_FILE, 'w')
    for w in words:
        f.write(w+'\n')
    f.close()

def add_word(word):
    words = read_file_to_list(WORD_FILE)
    if word in words:
        return False
    else:
        words.append(word)
        f = open(WORD_FILE, 'w')
        for w in words:
            f.write(w + '\n')
        f.close()
        return True
