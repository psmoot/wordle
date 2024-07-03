#!/usr/bin/env python3
#
# Let you know what words could solve a Wordle puzzle.
#
from english_words import get_english_words_set
from textwrap import dedent, fill

import unittest


def remove_letters(words: set, letter: str) -> set:
    """
    Return subset of words which do not have letter in them.
    """
    assert len(letter) == 1
    return [word for word in set(words) if letter not in word]


def remove_all_letters(words: set, letters: str) -> set:
    """
    Return a subset of words which contains none of the letters in letters in the words.
    """
    if letters != "NA":
        for letter in letters:
            words = remove_letters(words, letter)

    return words


def include_letters(words: set, letter: str) -> set:
    """
    Return set of words, all of which have a given letter somewhere in the word.
    """
    assert len(letter) == 1
    return [word for word in set(words) if letter in word]


def specific_letter(words: set, letter: str, placement: int) -> set:
    """
    Return list of all words where 'letter' is in the 'placement'th position.
    """
    assert len(letter) == 1
    return [word for word in words if word[placement] == letter]


def all_specific_letters(words: set, known_letters: str) -> set:
    # known_letters must be pairs of a letter and a digit so the length must be even.
    assert len(known_letters) % 2 == 0

    if known_letters != "NA":
        known_letters_list = list(known_letters)
        while len(known_letters_list) >= 2:
            letter = known_letters_list[0]
            position = int(known_letters_list[1]) - 1
            words = specific_letter(words, letter, position)
            known_letters_list = known_letters_list[2:]

    return words


def specific_not_letters(words: set, letter: str, placement: int):
    """
    Return set of words which do not have 'letter' in the word but not at the 'placement'th position.
    """
    assert len(letter) == 1
    return [word for word in words if letter in word and word[placement] != letter]


def remove_known_not_placed_letters(words: set, known_not_placed_letters: str) -> set:
    """
    Remove all words from set unless they contain a letter anywhere but the specified position.  These are letters
    we know are in the word but know they're not at a specific position.

    known_not_placed_letters is a string of letter, position pairs.  The letter is known to
    not be at the position.
    """
    assert len(known_not_placed_letters) % 2 == 0

    if known_not_placed_letters != "NA":
        not_placed_letters_list = list(known_not_placed_letters)
        while len(not_placed_letters_list) >= 2:
            letter = not_placed_letters_list[0]
            position = int(not_placed_letters_list[1]) - 1
            words = specific_not_letters(words, letter, position)
            not_placed_letters_list = not_placed_letters_list[2:]

    return words


def main():
    print("----")
    print("Hi! Welcome to the Wordle Solver.")

    cut_letters = input(
        dedent(
            """
                        Grey Letters
                        -----
                        Write the letters which are eliminated, or NA if there are none.  Do not use commas or separators.
                        """
        )
    )

    known_letters = input(
        dedent(
            """
                        Green Letters
                        ----
                        Write the letters which we know their place in the word, or NA if we don't know any
                        Use the format letter, placement, letter, placement;
                        for example, if we know 't' is the first letter and 's' is the fifth, input t1f5
                        """
        )
    )

    known_not_placed_letters = input(
        dedent(
            """
                                    Yellow Letters
                                    -----
                                    Write the letters which we know where they are NOT in the word, or NA if we don't know any.
                                    Use the format letter, placement, letter, placement;
                                    for example, if we know 'r' is NOT the first letter and 'p' is NOT the fifth, input r1p5
                                    """
        )
    )

    # Get starting list of five-letter English words which are not proper nouns.
    solutions = [
        word
        for word in get_english_words_set(["web2", "gcide"], alpha=True)
        if len(word) == 5 and word.islower()
    ]

    # Remove words which contain letters known not to be in answer.
    solutions = remove_all_letters(solutions, cut_letters)

    # Filter for words which contain letters at specified places
    solutions = all_specific_letters(solutions, known_letters)

    # fiter out words which have known incorrect placement of cut_letters
    solutions = remove_known_not_placed_letters(solutions, known_not_placed_letters)

    solutions.sort()
    print(f"There are {len(solutions)} options.")
    print("")
    print(
        f"Your {'first ten lines of ' if len(solutions) > 89 else ''}potential words are: "
    )
    print(
        fill(
            ", ".join(solutions),
            initial_indent="    ",
            subsequent_indent="    ",
            max_lines=10,
        )
    )

    print("Hope you enjoyed your experience with the Wordle Solver!\n")


if __name__ == "__main__":
    main()
