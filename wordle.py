#!/usr/bin/env python
# 
# Let you know what words could solve a Wordle puzzle.
#
from english_words import english_words_alpha_set

def remove_letters(words, letter):
    return [word for word in set(words) if letter not in word]

def include_letters(words, letter):
    return [word for word in set(words) if letter in word]

def specific_letters(words, letter, placement):
    return [word for word in set(words) if word[placement] == letter]

def specific_not_letters(words, letter, placement):
    return [word for word in set(words) if word[placement] != letter]

def main():
    print("----")
    print("Hi! Welcome to the Wordle Solver.")

    five_letters = [word for word in set(english_words_alpha_set) if len(word)==5]
    test_words = five_letters
    #test_words = ['hello', 'hi', 'goodday', 'gretchen']


    cut_letters = input("""
                        Grey Letters
                        -----
                        Write the letters which are eliminated, or NA if there are none.  Do not use commas or separators.
                        """)

    known_letters = input("""
                        Green Letters
                        ----
                        Write the letters which we know their place in the word, or NA if we don't know any
                        Use the format letter, placement, letter, placement;
                        for example, if we know 't' is the first letter and 's' is the fifth, input t1f5
                        """)

    known_not_placed_letters = input("""
                                    Yellow Letters
                                    -----
                                    Write the letters which we know where they are NOT in the word, or NA if we don't know any.
                                    Use the format letter, placement, letter, placement;
                                    for example, if we know 'r' is NOT the first letter and 'p' is NOT the fifth, input r1p5
                                    """)

    #remove letters which are not in the word
    if cut_letters != "NA":
        for letter in cut_letters:
            test_words = remove_letters(test_words, letter)

    #filter for words which contain included letters somewhere
    '''if yes_letters != "NA":
        for letter in yes_letters:
            test_words = include_letters(test_words, letter)
    '''

    #filter for words which contain letters at specified places
    if known_letters != "NA":
        usable_form = [item for item in known_letters]
        while len(usable_form) > 0:
            test_words = specific_letters(test_words, usable_form[0], int(usable_form[1])-1)
            usable_form = usable_form[2:]

    #fiter out words which have known incorrect placement of cut_letters
    if known_not_placed_letters != "NA":
        list_form = [item for item in known_not_placed_letters]
        while len(list_form) > 0:
            test_words = specific_not_letters(test_words, list_form[0], int(list_form[1])-1)
            list_form = list_form[2:]


    test_words.sort()
    test_words = [word for word in test_words if word.islower()]
    print(f"\nThere are {len(test_words)} options.")
    print("\nyour potential words are: ")
    for item in test_words:
        print(item)
    print("\nHope you enjoyed your experience with the Wordle Solver!\n")

if __name__ == '__main__':
    main()
