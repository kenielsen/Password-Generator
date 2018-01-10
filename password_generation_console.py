from password_generation import *

def main_menu():
    print("\n+----------------------------------------+")
    print("| Main Menu                              |")
    print("+----------------------------------------+")
    print("|  W = Word list manipulation            |")
    print("|  P = Password generation and retrieval |")
    print("|  X = eXit                              |")
    print("+----------------------------------------+")

def password_menu():
    print("\n+----------------------------------------+")
    print("| Password Menu                          |")
    print("+----------------------------------------+")
    print("|  C = Count passwords used              |")
    print("|  V = View password                     |")
    print("|  N = New password                      |")
    print("|  R = Return to Main Menu               |")
    print("+----------------------------------------+")

def password_methods(choice):
    if choice.upper() == "C":
        print("\nYou have used %d passwords" % count_combos())
    elif choice.upper() == "V":
        print("\nTo find a password by its index in the list,")
        print("enter a number between -{0} and {0}".format(count_combos()))
        try:
            idx = eval(input("Choice: "))
            if idx > 0: idx = idx - 1
            combo = get_combination(idx)
            print("\nPassword successfully retrieved!")
            password_display_menu(combo)
        except NameError:
            print("That is not a valid number.")
        pass
    elif choice.upper() == "N":
        sep = input("\nEnter separator: ")
        if sep == '':
            sep = "&"
        length = input("Enter number of words to choose: ")
        if length == '':
            length = 3
        else:
            try:
                length = int(length)
                if length > count_words():
                    print("Length cannot exceed the number of words.")
                else:
                    combo = generate_new_combination(sep, length)
                    print("\nPassword successfully generated!")
                    password_display_menu(combo)
            except ValueError:
                print("Length input was not a number.")
    else:
        print("\nInvalid choice!")

def word_menu():
    print("\n+----------------------------------------+")
    print("| Word List Menu                         |")
    print("+----------------------------------------+")
    print("|  C = Count words                       |")
    print("|  L = List words                        |")
    print("|  D = Delete word                       |")
    print("|  A = Add word                          |")
    print("|  R = Return to Main Menu               |")
    print("+----------------------------------------+")

def word_methods(choice):
    if choice.upper() == "C":
        print("\nThere are %d words in the list" % count_words())
    elif choice.upper() == "L":
        words = get_words()
        print("\nThe current word choices are:")
        for word in words:
            print('  ' + word)
    elif choice.upper() == "D":
        print("\nModifying the word list will change how the\ncombinations display.")
        if input("Are you sure you want to continue? (Y or N) ").upper() == "Y":
            word = input("\nEnter word you want to delete: ").lower()
            delete_word(word)
            print("\nThe word '%s' was successfully removed." % word)
    elif choice.upper() == "A":
        print("\nModifying the word list will change how the\ncombinations display.")
        if input("Are you sure you want to continue? (Y or N) ").upper() == "Y":
            word = input("Enter word you want to add: ").lower()
            if add_word(word):
                print("\nThe word '%s' was successfully added." % word)
    else:
        print("\nInvalid choice!")
    
def password_display_menu(combo):
    print("\n+----------------------------------------+")
    print("| Password Display Menu                  |")
    print("+----------------------------------------+")
    print("| F = Full text                          |")
    print("| H = Hidden                             |")
    print("| M = Masked                             |")
    print("+----------------------------------------+")
    print("| Default is Masked                      |")
    print("+----------------------------------------+")
    pick = input("Enter option: ")
    if pick.upper() == "F":
        print('\n' + combo.display(get_words()))
    elif pick.upper() == "H":
        print('\n' + combo.hide())
    else:
        print('\n' + combo.mask(get_words()))

def main():
    main = True
    password = False
    words = False
    print("Welcome to Password Generation!")
    while True:
        if main:
            main_menu()
        if password:
            password_menu()
        if words:
            word_menu()
        choice = input("\nEnter option: ")
        if main:
            if choice.upper() == "W":
                words = True
                main = False
            elif choice.upper() == "P":
                password = True
                main = False
            elif choice.upper() == "X":
                break
            else:
                print("Invalid choice!")
        else:
            if choice.upper() == "R":
                words = False
                password = False
                main = True
            elif words:
                word_methods(choice)
            elif password:
                password_methods(choice)
            
if __name__ == "__main__": main()
