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

    def test_specific_letters_1(self):
        filtered_words = specific_letters(TestSpecificLetters.test_words, 'a', 0)
        self.assertEqual(1, len(filtered_words))
        self.assertIn('apple', filtered_words)
        self.assertNotIn('bears', filtered_words)
        self.assertNotIn('words', filtered_words)
        self.assertNotIn('xyzzy', filtered_words)

    def test_specific_letters_2(self):
        filtered_words = specific_letters(TestSpecificLetters.test_words, 'a', 2)
        self.assertEqual(1, len(filtered_words))
        self.assertNotIn('apple', filtered_words)
        self.assertIn('bears', filtered_words)
        self.assertNotIn('words', filtered_words)
        self.assertNotIn('xyzzy', filtered_words)

    def test_specific_letters_len(self):
        with self.assertRaises(AssertionError):
            specific_letters(TestSpecificLetters.test_words, 'ab', 1)

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
            specific_letters(TestSpecificNotLetters.test_words, 'ab', 1)


if __name__ == '__main__':
    unittest.main()
