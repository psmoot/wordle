#!/usr/bin/env python3
# 
# Let you know what words could solve a Wordle puzzle.
#
import unittest
from wordle import *

class TestRemoveLetters(unittest.TestCase):
    test_words = [ 'apple', 'bears', 'words', 'xyzzy' ]

    def test_remove_letters_1(self):
        filtered_words = remove_letters(TestRemoveLetters.test_words, 'a')
        self.assertEqual(2, len(filtered_words))
        self.assertNotIn('apple', filtered_words)
        self.assertNotIn('bears', filtered_words)
        self.assertIn('words', filtered_words)
        self.assertIn('xyzzy', filtered_words)

    def test_remove_letters_2(self):
        filtered_words = remove_letters(TestRemoveLetters.test_words, 'q')
        self.assertEqual(4, len(filtered_words))

        for word in TestRemoveLetters.test_words:
            self.assertIn(word, filtered_words)

    def test_remove_letters_len(self):
        with self.assertRaises(AssertionError):
            remove_letters(TestRemoveLetters.test_words, 'ab')
    
class TestRemoveAllLetters(unittest.TestCase):
    test_words = [ 'apple', 'bears', 'words', 'xyzzy' ]

    def test_remove_all_letters_1(self):
        """
        Verify remove_all_letters() removes a single letter.
        """
        filtered_words = remove_all_letters(TestRemoveAllLetters.test_words, "a")
        self.assertEqual(2, len(filtered_words))
        self.assertNotIn('apple', filtered_words)
        self.assertNotIn('bears', filtered_words)
        self.assertIn('words', filtered_words)
        self.assertIn('xyzzy', filtered_words)

    def test_remove_all_letters_2(self):
        """
        Verify remove_all_letters() can remove two different letters.
        """
        filtered_words = remove_all_letters(TestRemoveAllLetters.test_words, "wz")
        self.assertEqual(2, len(filtered_words))
        self.assertIn('apple', filtered_words)
        self.assertIn('bears', filtered_words)
        self.assertNotIn('words', filtered_words)
        self.assertNotIn('xyzzy', filtered_words)

    def test_remove_all_letters_3(self):
        """
        Verify remove_all_letters() does nothing when passed 'NA' as the letters to remove.
        """
        filtered_words = remove_all_letters(TestRemoveAllLetters.test_words, "NA")
        self.assertEqual(4, len(filtered_words))
        self.assertIn('apple', filtered_words)
        self.assertIn('bears', filtered_words)
        self.assertIn('words', filtered_words)
        self.assertIn('xyzzy', filtered_words)

    def test_remove_all_letters_2(self):
        """
        Verify remove_all_letters does nothing when none of the words match the letters to cut.
        """
        filtered_words = remove_all_letters(TestRemoveAllLetters.test_words, "qt")
        self.assertEqual(4, len(filtered_words))
        self.assertIn('apple', filtered_words)
        self.assertIn('bears', filtered_words)
        self.assertIn('words', filtered_words)
        self.assertIn('xyzzy', filtered_words)

class TestIncludeLetters(unittest.TestCase):
    test_words = [ 'apple', 'bear', 'words', 'xyzzy' ]

    def test_include_letters_1(self):
        filtered_words = include_letters(TestIncludeLetters.test_words, 'a')
        self.assertEqual(2, len(filtered_words))
        self.assertIn('apple', filtered_words)
        self.assertIn('bear', filtered_words)
        self.assertNotIn('words', filtered_words)
        self.assertNotIn('xyzzy', filtered_words)

    def test_include_letters_len(self):
        with self.assertRaises(AssertionError):
            include_letters(TestIncludeLetters.test_words, 'ab')

class TestSpecificLetters(unittest.TestCase):
    test_words = [ 'apple', 'bears', 'words', 'xyzzy' ]

    def test_specific_letter_1(self):
        filtered_words = specific_letter(TestSpecificLetters.test_words, 'a', 0)
        self.assertEqual(1, len(filtered_words))
        self.assertIn('apple', filtered_words)
        self.assertNotIn('bears', filtered_words)
        self.assertNotIn('words', filtered_words)
        self.assertNotIn('xyzzy', filtered_words)

    def test_specific_letter_2(self):
        filtered_words = specific_letter(TestSpecificLetters.test_words, 'a', 2)
        self.assertEqual(1, len(filtered_words))
        self.assertNotIn('apple', filtered_words)
        self.assertIn('bears', filtered_words)
        self.assertNotIn('words', filtered_words)
        self.assertNotIn('xyzzy', filtered_words)

    def test_specific_letter_len(self):
        with self.assertRaises(AssertionError):
            specific_letter(TestSpecificLetters.test_words, 'ab', 1)

class TestAllSpecificLetters(unittest.TestCase):
    test_words = [ 'apple', 'abcde', 'bears', 'words', 'xyzzy' ]

    def test_all_specific_letters_1(self):
        filtered_words = all_specific_letters(TestAllSpecificLetters.test_words, 'a1')
        self.assertEqual(2, len(filtered_words))
        self.assertIn('apple', filtered_words)
        self.assertIn('abcde', filtered_words)
        self.assertNotIn('bears', filtered_words)
        self.assertNotIn('words', filtered_words)
        self.assertNotIn('xyzzy', filtered_words)

    def test_all_specific_letters_2(self):
        filtered_words = all_specific_letters(TestAllSpecificLetters.test_words, 'a1b2')
        self.assertEqual(1, len(filtered_words))
        self.assertNotIn('apple', filtered_words)
        self.assertIn('abcde', filtered_words)
        self.assertIn('bears', filtered_words)
        self.assertNotIn('words', filtered_words)
        self.assertNotIn('xyzzy', filtered_words)

    def test_all_specific_letters_2(self):
        filtered_words = all_specific_letters(TestAllSpecificLetters.test_words, 'NA')
        self.assertEqual(5, len(filtered_words))
        self.assertIn('apple', filtered_words)
        self.assertIn('abcde', filtered_words)
        self.assertIn('bears', filtered_words)
        self.assertIn('words', filtered_words)
        self.assertIn('xyzzy', filtered_words)

    def test_all_specific_letters_len(self):
        with self.assertRaises(AssertionError):
            all_specific_letters(TestSpecificLetters.test_words, 'a')

class TestSpecificNotLetters(unittest.TestCase):
    test_words = [ 'apple', 'bears', 'words', 'xyzzy' ]

    def test_specific_not_letters_1(self):
        filtered_words = specific_not_letters(TestSpecificNotLetters.test_words, 'a', 0)
        self.assertEqual(3, len(filtered_words))
        self.assertNotIn('apple', filtered_words)
        self.assertIn('bears', filtered_words)
        self.assertIn('words', filtered_words)
        self.assertIn('xyzzy', filtered_words)

    def test_specific_not_letters_2(self):
        filtered_words = specific_not_letters(TestSpecificNotLetters.test_words, 'a', 2)
        self.assertEqual(3, len(filtered_words))
        self.assertIn('apple', filtered_words)
        self.assertNotIn('bears', filtered_words)
        self.assertIn('words', filtered_words)
        self.assertIn('xyzzy', filtered_words)

    def test_remove_letters_len(self):
        with self.assertRaises(AssertionError):
            specific_letter(TestSpecificNotLetters.test_words, 'ab', 1)

class TestRemoveKnownNotPlacedLetters(unittest.TestCase):
    test_words = [ 'apple', 'bears', 'words', 'xyzzy' ]

    def test_known_not_placed_na(self):
        filtered_words = remove_known_not_placed_letters(TestRemoveKnownNotPlacedLetters.test_words, 'NA')
        self.assertEqual(4, len(filtered_words))
        self.assertIn('apple', filtered_words)
        self.assertIn('bears', filtered_words)
        self.assertIn('words', filtered_words)
        self.assertIn('xyzzy', filtered_words)

    def test_known_not_placed_all(self):
        filtered_words = remove_known_not_placed_letters(TestRemoveKnownNotPlacedLetters.test_words, 'q1')
        self.assertEqual(0, len(filtered_words))
        self.assertNotIn('apple', filtered_words)
        self.assertNotIn('bears', filtered_words)
        self.assertNotIn('words', filtered_words)
        self.assertNotIn('xyzzy', filtered_words)

    def test_known_not_placed_1(self):
        filtered_words = remove_known_not_placed_letters(TestRemoveKnownNotPlacedLetters.test_words, 'a1')
        self.assertEqual(1, len(filtered_words))
        self.assertNotIn('apple', filtered_words)
        self.assertIn('bears', filtered_words)
        self.assertNotIn('words', filtered_words)
        self.assertNotIn('xyzzy', filtered_words)

    def test_known_not_placed_2(self):
        filtered_words = remove_known_not_placed_letters(TestRemoveKnownNotPlacedLetters.test_words, 'a5')
        self.assertEqual(2, len(filtered_words))
        self.assertIn('apple', filtered_words)
        self.assertIn('bears', filtered_words)
        self.assertNotIn('words', filtered_words)
        self.assertNotIn('xyzzy', filtered_words)

if __name__ == '__main__':
    unittest.main()
